from typing import Any, Optional, Type

from django.db import models as django_models
from drive_bot_proto import client_pb2 as pb
from drive_bot_proto.client_pb2_grpc import DriveBotServiceServicer
from pydantic import BaseModel, Field

from drive.bot.const import Language
from drive.exam import models
from drive.exam.filters import v1 as filters
from drive.exam.utils import download_image, get_mime_type
from drive.server_grpc.utils import MessageLike, Model, ProtoFilterMixin, ProtoWrapper

from .exceptions import DefaultProtoMessageException


class QuerySetResponse(BaseModel):
    qs: django_models.QuerySet[Model]
    count: int

    class Config:
        arbitrary_types_allowed = True


class _Context(BaseModel):
    limit: Optional[int] = Field(alias="limit", default=1000)
    offset: Optional[int] = Field(alias="offset", default=0)
    lang: str = Field(alias="lang")

    @classmethod
    def _get_language(cls, message: MessageLike, context) -> str:
        language_mapping = {
            # pb.Language.LANG_AZ: Language.AZERBAIJANI.value,
            pb.Language.LANG_EN: Language.ENGLISH.value,
            # pb.Language.LANG_HY: Language.ARMENIAN.value,
            pb.Language.LANG_KA: Language.GEORGIAN.value,
            pb.Language.LANG_RU: Language.RUSSIAN.value,
            # pb.Language.LANG_TR: Language.TURKISH.value,
            pb.Language.LANG_UK: Language.UKRAINIAN.value,
        }
        if hasattr(message, "lang"):
            return language_mapping.get(message.lang, context.main_language)
        return context.main_language

    @classmethod
    def parse_proto(cls, message: MessageLike, context: any) -> "_Context":
        message = ProtoWrapper.parse_proto(message)
        limit = getattr(message, "limit", 100) or 100
        offset = getattr(message, "offset", 0) or 0
        return cls(
            limit=limit,
            offset=offset,
            lang=cls._get_language(message, context),
        )


class DriveBotServiceGRPC(DriveBotServiceServicer, ProtoFilterMixin):
    filters_mapping = {
        pb.GetTicketsRequest: filters.TicketFilter,
        pb.GetAnswersRequest: filters.AnswerFilter,
    }

    @staticmethod
    def _map_ticket_instance_to_proto(ticket: models.Ticket, context: _Context) -> pb.Ticket:
        return pb.Ticket(
            id=ticket.id,
            external_id=ticket.external_id,
            question=ticket.question.get(context.lang),
            image_id=ticket.image.id if ticket.image else None,
            description=ticket.description.get(context.lang),
            categories=ticket.categories.all().values_list("id", flat=True),
            topic_id=ticket.topic.id,
        )

    @staticmethod
    def _map_answer_instance_to_proto(answer: models.Answer, context: _Context) -> pb.Answer:
        return pb.Answer(
            id=answer.id,
            ticket_id=answer.ticket.id,
            answer=answer.answer.get(context.lang),
            is_valid=answer.is_valid,
        )

    @staticmethod
    def _map_category_instance_to_proto(
        category: models.TicketCategory, context: _Context
    ) -> pb.Category:
        return pb.Category(
            id=category.id,
            name=category.name.get(context.lang),
            description=category.description.get(context.lang),
        )

    @staticmethod
    def _map_topic_instance_to_proto(topic: models.TicketTopic, context: _Context) -> pb.Topic:
        return pb.Topic(
            id=topic.id,
            name=topic.name.get(context.lang),
        )

    @staticmethod
    def _raise_error(message: Type[MessageLike]):
        response = message(error="Not found")
        raise DefaultProtoMessageException(response)

    def _get_items_by_model(
        self, model: Type[Model], request: MessageLike, context: Any
    ) -> QuerySetResponse:
        filter_class = self.filters_mapping.get(type(request))
        qs = model.objects.all().order_by("id")
        if filter_class:
            qs = self._filter_queryset(qs, filter_class, request)
        return QuerySetResponse(qs=qs, count=qs.count())

    def _get_single_item(
        self,
        model: Type[Model],
        request: pb.GetEntityByIdRequest,
        error_response: Type[MessageLike],
    ) -> Model:
        try:
            instance = model.objects.get(id=request.id)
        except model.DoesNotExist:
            self._raise_error(error_response)
        else:
            return instance

    @staticmethod
    def _paginate_queryset(
        queryset: django_models.QuerySet[Model], limit: int, offset: int
    ) -> django_models.QuerySet[Model]:
        return queryset[offset : offset + limit]

    def GetTickets(self, request: pb.GetTicketsRequest, context: Any) -> pb.GetTicketsResponse:
        context = _Context.parse_proto(request, context)
        qs_data = self._get_items_by_model(models.Ticket, request, context)
        items = self._paginate_queryset(qs_data.qs, context.limit, context.offset)
        tickets = []
        for ticket in items:
            tickets.append(self._map_ticket_instance_to_proto(ticket, context))
        response = pb.GetTicketsResponse(tickets=tickets, count=qs_data.count)
        return response

    def GetAnswers(self, request: pb.GetAnswersRequest, context: Any) -> pb.GetAnswersResponse:
        context = _Context.parse_proto(request, context)
        qs_data = self._get_items_by_model(models.Answer, request, context)
        items = self._paginate_queryset(qs_data.qs, context.limit, context.offset)
        answers = []
        for answer in items:
            answers.append(self._map_answer_instance_to_proto(answer, context))
        response = pb.GetAnswersResponse(answers=answers, count=qs_data.count)
        return response

    def GetCategories(self, request: pb.BaseRequest, context: Any) -> pb.GetCategoriesResponse:
        context = _Context.parse_proto(request, context)
        qs_data = self._get_items_by_model(models.TicketCategory, request, context)
        items = self._paginate_queryset(qs_data.qs, context.limit, context.offset)
        categories = []
        for category in items:
            categories.append(self._map_category_instance_to_proto(category, context))
        response = pb.GetCategoriesResponse(categories=categories, count=qs_data.count)
        return response

    def GetTopics(self, request: pb.BaseRequest, context: Any) -> pb.GetTopicsResponse:
        context = _Context.parse_proto(request, context)
        qs_data = self._get_items_by_model(models.TicketTopic, request, context)
        items = self._paginate_queryset(qs_data.qs, context.limit, context.offset)
        topics = []
        for topic in items:
            topics.append(self._map_topic_instance_to_proto(topic, context))
        response = pb.GetTopicsResponse(topics=topics, count=qs_data.count)
        return response

    def GetImageById(
        self, request: pb.GetEntityByIdRequest, context: Any
    ) -> pb.GetImageByIdResponse:
        try:
            image = self._get_single_item(models.TicketImage, request, pb.GetImageByIdResponse)
        except DefaultProtoMessageException as error:
            return error.proto_message
        image_bytes = download_image(image, False)
        mime_type = get_mime_type(image)
        return pb.GetImageByIdResponse(image=pb.Image(image_bytes=image_bytes, mime_type=mime_type))

    def GetTicketById(
        self, request: pb.GetEntityByIdRequest, context: Any
    ) -> pb.GetTicketByIdResponse:
        context = _Context.parse_proto(request, context)
        try:
            ticket = self._get_single_item(models.Ticket, request, pb.GetTicketByIdResponse)
        except DefaultProtoMessageException as error:
            return error.proto_message
        response = pb.GetTicketByIdResponse(
            ticket=self._map_ticket_instance_to_proto(ticket, context)
        )
        return response

    def GetAnswerById(
        self, request: pb.GetEntityByIdRequest, context: Any
    ) -> pb.GetAnswerByIdResponse:
        context = _Context.parse_proto(request, context)
        try:
            answer = self._get_single_item(models.Answer, request, pb.GetAnswerByIdResponse)
        except DefaultProtoMessageException as error:
            return error.proto_message
        response = pb.GetAnswerByIdResponse(
            answer=self._map_answer_instance_to_proto(answer, context)
        )
        return response

    def GetCategoryById(
        self, request: pb.GetEntityByIdRequest, context: Any
    ) -> pb.GetCategoryByIdResponse:
        context = _Context.parse_proto(request, context)
        try:
            category = self._get_single_item(
                models.TicketCategory, request, pb.GetCategoryByIdResponse
            )
        except DefaultProtoMessageException as error:
            return error.proto_message
        response = pb.GetCategoryByIdResponse(
            category=self._map_category_instance_to_proto(category, context)
        )
        return response

    def GetTopicById(
        self, request: pb.GetEntityByIdRequest, context: Any
    ) -> pb.GetTopicByIdResponse:
        context = _Context.parse_proto(request, context)
        try:
            topic = self._get_single_item(models.TicketTopic, request, pb.GetTopicByIdResponse)
        except DefaultProtoMessageException as error:
            return error.proto_message
        response = pb.GetTopicByIdResponse(topic=self._map_topic_instance_to_proto(topic, context))
        return response
