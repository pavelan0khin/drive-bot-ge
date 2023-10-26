from django.db import models

from drive.bot.models import User
from drive.utils.common import boolean_choices
from drive.utils.models import BaseModel

from .answer import Answer
from .session import Session
from .ticket import Ticket


class TicketHistory(BaseModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="tickets_history",
    )
    session = models.ForeignKey(to=Session, on_delete=models.CASCADE)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE, null=True, blank=True)
    is_valid = models.BooleanField(
        verbose_name="Is valid?",
        choices=boolean_choices,
        null=True,
        blank=True,
    )
    bot_message_id = models.BigIntegerField(verbose_name="Bot Message ID", null=True, blank=True)

    class Meta:
        verbose_name = "Ticket history"
        verbose_name_plural = "Tickets history"
