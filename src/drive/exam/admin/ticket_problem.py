from django.contrib import admin

from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.TicketProblem)
class TicketProblemAdmin(BaseAdmin):
    list_display = (
        "id",
        "user",
        "ticket",
        "user_message_id",
        "bot_message_id",
        "wants_answer",
        "is_resolved",
        "created_at",
        "updated_at",
    )

    list_display_links = list_display

    list_filter = ("user", "is_resolved", "created_at", "updated_at", "wants_answer")

    readonly_fields = ("created_at", "updated_at")
