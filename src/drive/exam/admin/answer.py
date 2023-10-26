from django.contrib import admin
from django.template.defaultfilters import truncatechars

from drive.bot.const import Language
from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.Answer)
class AnswerAdmin(BaseAdmin):
    list_display = (
        "id",
        "ticket",
        "en_answer",
        "is_valid",
        "created_at",
        "updated_at",
    )

    list_display_links = list_display

    list_filter = ("ticket", "is_valid", "created_at", "updated_at")

    search_fields = ("ticket__question__ru", "answer__r")

    readonly_fields = ("created_at", "updated_at")

    def en_answer(self, obj):
        return truncatechars(obj.answer.get("en", "No data"), 25)

    en_answer.short_description = "Answer"

    def get_changeform_initial_data(self, request):
        initial_data = super().get_changeform_initial_data(request)
        initial_data["answer"] = Language.get_initial_json()
        return initial_data
