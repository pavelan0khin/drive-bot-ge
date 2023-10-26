from django.db import models

from drive.utils.common import boolean_choices
from drive.utils.models import BaseModel


class Setting(BaseModel):
    working = models.BooleanField(
        verbose_name="Bot working?", default=True, choices=boolean_choices
    )
    not_working_reason = models.JSONField(verbose_name="Not working reason", null=True, blank=True)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"

    def __str__(self):
        return f"Working: {self.working}"
