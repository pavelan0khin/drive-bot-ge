from django.db import models

from drive.utils.models import BaseModel

from .user import User


class State(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User")
    state = models.CharField(verbose_name="State", max_length=128)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.state
