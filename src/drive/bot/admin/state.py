from django.contrib import admin

from drive.bot import models
from drive.utils.admin import BaseAdmin


@admin.register(models.State)
class StateAdmin(BaseAdmin):
    list_display = ("id", "user", "state", "created_at", "updated_at")

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")

    search_fields = (
        "state",
        "user__first_name",
        "user__username",
        "user__last_name",
    )
