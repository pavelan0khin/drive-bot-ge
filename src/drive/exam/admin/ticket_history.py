from django.contrib import admin

from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.TicketHistory)
class TicketHistoryAdmin(BaseAdmin):
    list_display = (
        "id",
        "user",
        "session",
        "ticket",
        "selected_answer",
        "is_valid",
    )

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")

    readonly_fields = (
        "user",
        "session",
        "ticket",
        "selected_answer",
        "created_at",
        "updated_at",
    )
