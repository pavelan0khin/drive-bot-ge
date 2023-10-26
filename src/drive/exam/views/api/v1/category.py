from drive.api.views import BaseModelViewSet
from drive.exam import models
from drive.exam.filters.v1 import BaseFilterSet
from drive.exam.serializers.v1 import CategorySerializer


class CategoryViewSet(BaseModelViewSet):
    queryset = models.TicketCategory.objects.all().order_by("id")
    serializer_class = CategorySerializer
    filterset_class = BaseFilterSet
