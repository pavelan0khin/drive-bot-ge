from django.db import models
from django.template.defaultfilters import truncatechars

from drive.exam.models.ticket import Ticket
from drive.utils.common import boolean_choices
from drive.utils.fields import JSONField
from drive.utils.models import BaseModel


class Answer(BaseModel):
    ticket = models.ForeignKey(
        to=Ticket,
        on_delete=models.CASCADE,
        verbose_name="Question",
        related_name="answers",
    )
    answer = JSONField(verbose_name="Answer")
    is_valid = models.BooleanField(verbose_name="Is valid?", choices=boolean_choices)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return truncatechars(self.answer.get("ru"), 25)
