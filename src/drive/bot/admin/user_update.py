from django.contrib import admin

from drive.bot import models
from drive.utils.admin import BaseAdmin


@admin.register(models.UserUpdate)
class UserUpdateAdmin(BaseAdmin):
    list_display = ("id", "user", "created_at", "updated_at")

    list_display_links = list_display

    list_filter = ("created_at", "updated_at")
