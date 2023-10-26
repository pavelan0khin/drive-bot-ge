from django.db import models
from django.utils import timezone

from drive.bot.models import User
from drive.exam.const import SessionType
from drive.utils.common import boolean_choices
from drive.utils.models import BaseModel

from .ticket import Ticket
from .ticket_category import TicketCategory


class Session(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User")
    session_type = models.CharField(
        verbose_name="Session type", max_length=32, choices=SessionType.choices
    )
    category = models.ForeignKey(
        to=TicketCategory,
        on_delete=models.CASCADE,
        verbose_name="Category",
        null=True,
    )
    tickets = models.ManyToManyField(to=Ticket, related_name="sessions", verbose_name="Tickets")
    valid_solved_tickets = models.ManyToManyField(
        to=Ticket,
        related_name="exams_with_valid_solved",
        verbose_name="Valid solved tickets",
    )
    invalid_solved_tickets = models.ManyToManyField(
        to=Ticket,
        related_name="exams_with_invalid_solved",
        verbose_name="Invalid solved tickets",
    )
    finished_at = models.DateTimeField(verbose_name="Finished at", null=True, blank=True)
    is_declined = models.BooleanField(
        verbose_name="Is declined?", default=False, choices=boolean_choices
    )

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __str__(self):
        return f"{self.user} | {self.session_type} #{self.id}"

    def add_category(self, category: TicketCategory) -> None:
        self.category = category
        self.save()

    def set_as_declined(self) -> None:
        self.tickets.clear()
        self.invalid_solved_tickets.clear()
        self.valid_solved_tickets.clear()
        self.is_declined = True
        self.finished_at = timezone.now()
        self.save()
