from django.contrib import admin
from django.template.defaultfilters import truncatechars

from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.TicketImage)
class TicketImageAdmin(BaseAdmin):
    list_display = ("id", "image", "file_id", "created_at", "updated_at")

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")

    search_fields = ("image",)

    readonly_fields = ("created_at", "updated_at")
