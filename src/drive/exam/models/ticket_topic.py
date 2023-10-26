from django.db import models

from drive.utils.fields import JSONField
from drive.utils.models import BaseModel


class TicketTopic(BaseModel):
    topic_id = models.PositiveIntegerField(verbose_name="Topic ID")
    name = JSONField(verbose_name="Name")

    class Meta:
        verbose_name = "Ticket Topic"
        verbose_name_plural = "Ticket Topics"
        ordering = ["id"]

    def __str__(self):
        return f"{self.topic_id}. {self.name.get('ru')}"
