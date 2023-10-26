from django.contrib import admin
from django.template.defaultfilters import truncatechars

from drive.bot.const import Language
from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.TicketTopic)
class TicketTopicAdmin(BaseAdmin):
    list_display = ("id", "topic_id", "en_name", "created_at", "updated_at")

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")

    search_fields = ("image",)

    readonly_fields = ("created_at", "updated_at")

    def en_name(self, obj):
        return truncatechars(obj.name.get("en", "No data"), 25)

    en_name.short_description = "Name"

    def get_changeform_initial_data(self, request):
        initial_data = super().get_changeform_initial_data(request)
        initial_data["name"] = Language.get_initial_json()
        return initial_data
