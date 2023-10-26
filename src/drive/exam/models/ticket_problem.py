from django.db import models

from drive.bot.models import User
from drive.exam.models.ticket import Ticket
from drive.utils.common import boolean_choices
from drive.utils.models import BaseModel


class TicketProblem(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User")
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, verbose_name="Ticket")
    user_message_id = models.PositiveBigIntegerField(verbose_name="User message id")
    bot_message_id = models.PositiveIntegerField(verbose_name="Bot message id", null=True)
    text = models.TextField(verbose_name="Text")
    wants_answer = models.BooleanField(
        verbose_name="Wants answer?", choices=boolean_choices, default=False
    )
    is_resolved = models.BooleanField(
        verbose_name="Resolved?", choices=boolean_choices, default=False
    )

    class Meta:
        verbose_name = "Ticket problem"
        verbose_name_plural = "Ticket problems"
