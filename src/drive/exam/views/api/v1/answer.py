from drive.api.views import BaseModelViewSet
from drive.exam import models
from drive.exam.filters.v1 import AnswerFilter
from drive.exam.serializers.v1 import AnswerSerializer


class AnswerViewSet(BaseModelViewSet):
    queryset = models.Answer.objects.all().order_by("id")
    serializer_class = AnswerSerializer
    filterset_class = AnswerFilter
