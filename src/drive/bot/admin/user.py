from django.contrib import admin

from drive.bot import models
from drive.utils.admin import BaseAdmin


@admin.register(models.User)
class UserAdmin(BaseAdmin):
    list_display = (
        "id",
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "created_at",
        "updated_at",
    )

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")

    search_fields = ("telegram_id", "username", "first_name", "last_name")
