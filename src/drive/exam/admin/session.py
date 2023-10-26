from django.contrib import admin

from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.Session)
class SessionAdmin(BaseAdmin):
    list_display = (
        "id",
        "user",
        "session_type",
        "created_at",
        "updated_at",
        "finished_at",
    )

    list_display_links = list_display

    list_filter = ("session_type", "created_at", "updated_at", "finished_at")

    readonly_fields = (
        "tickets",
        "valid_solved_tickets",
        "invalid_solved_tickets",
        "created_at",
        "updated_at",
        "finished_at",
    )
