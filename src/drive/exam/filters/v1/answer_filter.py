import django_filters as df

from drive.exam import models

from .base import BaseFilterSet


class AnswerFilter(BaseFilterSet):
    ticket_id = df.NumberFilter(field_name="ticket", lookup_expr="exact")
    is_valid = df.BooleanFilter(field_name="is_valid", lookup_expr="exact")

    class Meta:
        model = models.Answer
        fields = ["ticket_id", "is_valid"]
