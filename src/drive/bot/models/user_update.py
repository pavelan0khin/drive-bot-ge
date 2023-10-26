from django.db import models

from drive.utils.models import BaseModel

from .user import User


class UserUpdate(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User")
    updates = models.JSONField(verbose_name="User Updates")

    class Meta:
        verbose_name = "User Update"
        verbose_name_plural = "User Updates"

    def __str__(self):
        return f"Update ID {self.id} for {self.user}"
