from django.contrib import admin
from django.template.defaultfilters import truncatechars

from drive.bot.const import Language
from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.Ticket)
class TicketAdmin(BaseAdmin):
    list_display = (
        "id",
        "external_id",
        "topic",
        "en_question",
        "image",
        "en_description",
        "created_at",
        "updated_at",
    )

    list_display_links = list_display

    list_filter = ("topic", "categories", "created_at", "updated_at")

    search_fields = ("question__ru", "description__ru")

    readonly_fields = ("created_at", "updated_at")

    def en_question(self, obj):
        return truncatechars(obj.question.get("en", "No data"), 25)

    def en_description(self, obj):
        return truncatechars(obj.description.get("en", "No data"), 25)

    en_question.short_description = "Question"
    en_description.short_description = "Description"

    def get_changeform_initial_data(self, request):
        initial_data = super().get_changeform_initial_data(request)
        initial_json = Language.get_initial_json()
        initial_data["question"] = initial_json
        initial_data["description"] = initial_json
        return initial_data
