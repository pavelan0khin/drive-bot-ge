from django.db import models

from drive.utils.fields import JSONField
from drive.utils.models import BaseModel


class TicketCategory(BaseModel):
    category_id = models.PositiveIntegerField(verbose_name="Category ID")
    name = JSONField(verbose_name="Name", max_length=128, unique=True)
    description = JSONField(verbose_name="Description", null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.get("ru")
