from django.contrib import admin

from drive.bot import models
from drive.bot.const import Language
from drive.utils.admin import BaseAdmin


@admin.register(models.Setting)
class SettingAdmin(BaseAdmin):
    list_display = ("working",)
    list_display_links = list_display
    readonly_fields = ("created_at", "updated_at")

    def get_changeform_initial_data(self, request):
        initial_data = super().get_changeform_initial_data(request)
        initial_data["not_working_reason"] = Language.get_initial_json()
        return initial_data
