from django.db import models

from drive.bot.const import Language
from drive.utils.common import boolean_choices
from drive.utils.models import BaseModel


class User(BaseModel):
    telegram_id = models.PositiveBigIntegerField(verbose_name="Telegram ID", unique=True)
    username = models.CharField(max_length=32, verbose_name="Username", null=True, blank=True)
    first_name = models.CharField(max_length=64, verbose_name="First name")
    last_name = models.CharField(max_length=64, verbose_name="Last name", null=True, blank=True)
    language_code = models.CharField(
        max_length=4, verbose_name="Language Code", null=True, blank=True
    )
    main_language = models.CharField(
        max_length=2,
        verbose_name="Main Language",
        default=Language.ENGLISH,
        choices=Language.choices,
    )
    wants_notifications = models.BooleanField(
        verbose_name="Wants notifications?",
        default=False,
        choices=boolean_choices,
    )
    know_about_chosen_answer = models.BooleanField(
        verbose_name="Know about chosen answer?",
        default=False,
        choices=boolean_choices,
    )
    is_blocked = models.BooleanField(
        verbose_name="Is blocked?", default=False, choices=boolean_choices
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        if self.username:
            return f"{self.telegram_id} | {self.username}"
        return f"{self.telegram_id} {self.first_name}"
