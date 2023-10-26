from abc import ABC, abstractmethod
from typing import Any, Dict, Type, TypeVar, cast
from urllib.parse import urlencode

from django.db import models as django_models
from django.http import QueryDict
from django_filters import FilterSet
from google.protobuf.descriptor_pb2 import FieldDescriptorProto
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message

MessageLike = TypeVar("MessageLike", bound=Message)

Model = TypeVar("Model", bound=django_models.Model)


class ProtoWrapper:
    _allowed_field_types = (
        FieldDescriptorProto.Type.TYPE_DOUBLE,
        FieldDescriptorProto.Type.TYPE_FLOAT,
        FieldDescriptorProto.Type.TYPE_INT32,
        FieldDescriptorProto.Type.TYPE_INT64,
        FieldDescriptorProto.Type.TYPE_UINT32,
        FieldDescriptorProto.Type.TYPE_UINT64,
        FieldDescriptorProto.Type.TYPE_SINT32,
        FieldDescriptorProto.Type.TYPE_SINT64,
        FieldDescriptorProto.Type.TYPE_FIXED32,
        FieldDescriptorProto.Type.TYPE_FIXED64,
        FieldDescriptorProto.Type.TYPE_SFIXED32,
        FieldDescriptorProto.Type.TYPE_SFIXED64,
        FieldDescriptorProto.Type.TYPE_BOOL,
        FieldDescriptorProto.Type.TYPE_STRING,
        FieldDescriptorProto.Type.TYPE_BYTES,
    )

    @classmethod
    def parse_proto(cls, message: MessageLike) -> MessageLike:
        custom_instance = cls()
        class_fields = message.DESCRIPTOR.fields_by_name
        for field_name, field_descriptor in class_fields.items():
            value = getattr(message, field_name)
            if field_descriptor.type in cls._allowed_field_types:
                try:
                    has_field = message.HasField(field_name)
                except ValueError:
                    has_field = True
                if has_field:
                    setattr(custom_instance, field_name, value)
                else:
                    setattr(custom_instance, field_name, None)
            else:
                setattr(custom_instance, field_name, value)
        return cast(MessageLike, custom_instance)


class ProtoFilterMixin(ABC):
    @property
    @abstractmethod
    def filters_mapping(self) -> Dict[Any, Any]:
        pass

    _forbidden_dict_keys = ["limit", "offset", "lang"]

    def _proto_to_query_dict(self, proto: MessageLike) -> QueryDict:
        original_dict = MessageToDict(proto, False, True, True)
        for key in self._forbidden_dict_keys:
            if key in original_dict:
                original_dict.pop(key)
        query_dict = QueryDict(urlencode(original_dict, doseq=True), mutable=True)
        return query_dict

    def _filter_queryset(
        self,
        qs: django_models.QuerySet[Type[Model]],
        filter_class: Type[FilterSet],
        proto: MessageLike,
    ) -> django_models.QuerySet[Model]:
        filters_as_query_dict = self._proto_to_query_dict(proto)
        model_filter = filter_class(filters_as_query_dict, queryset=qs)
        qs = model_filter.filter_queryset(qs)
        return qs
