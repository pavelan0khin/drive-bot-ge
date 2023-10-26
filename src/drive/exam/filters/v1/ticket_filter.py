import django_filters as df

from drive.exam import models

from .base import BaseFilterSet, NumberArrayExactFilter, NumberArrayInFilter


class TicketFilter(BaseFilterSet):
    external_id = df.NumberFilter(field_name="external_id", lookup_expr="exact")
    categories_ids = NumberArrayExactFilter(field_name="categories", lookup_expr="exact")
    topic_ids = NumberArrayInFilter(field_name="topic__id", lookup_expr="in")

    class Meta:
        model = models.Ticket
        fields = ["external_id", "categories_ids", "topic_ids"]
