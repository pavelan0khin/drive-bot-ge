from drive.api.views import BaseModelViewSet
from drive.exam import models
from drive.exam.filters.v1 import TicketFilter
from drive.exam.serializers.v1 import TicketSerializer


class TicketViewSet(BaseModelViewSet):
    queryset = models.Ticket.objects.all().order_by("external_id")
    serializer_class = TicketSerializer
    filterset_class = TicketFilter
