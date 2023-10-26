from drive.api.views import BaseModelViewSet
from drive.exam import models
from drive.exam.filters.v1 import BaseFilterSet
from drive.exam.serializers.v1 import TopicSerializer


class TopicViewSet(BaseModelViewSet):
    queryset = models.TicketTopic.objects.all().order_by("id")
    serializer_class = TopicSerializer
    filterset_class = BaseFilterSet
