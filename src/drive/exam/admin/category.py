from django.contrib import admin

from drive.bot.const import Language
from drive.exam import models
from drive.utils.admin import BaseAdmin


@admin.register(models.TicketCategory)
class CategoryAdmin(BaseAdmin):
    list_display = (
        "id",
        "category_id",
        "en_name",
        "en_description",
        "created_at",
        "updated_at",
    )

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")

    def en_name(self, obj):
        return obj.name.get("en", "No data")

    def en_description(self, obj):
        return obj.description.get("en", "No data")

    en_name.short_description = "Name"
    en_description.short_description = "Description"

    def get_changeform_initial_data(self, request):
        initial_data = super().get_changeform_initial_data(request)
        initial_json = Language.get_initial_json()
        initial_data["name"] = initial_json
        initial_data["description"] = initial_json
        return initial_data
