import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

from drive.utils.models import BaseModel

from .user import User


class APIToken(BaseModel):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User,
        related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    class Meta:
        abstract = False
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
