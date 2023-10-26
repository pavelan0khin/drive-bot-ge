from django.contrib import admin
from rest_framework.authtoken.models import Token

from drive.bot import models


@admin.register(models.APIToken)
class APITokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "created_at", "updated_at")
    list_display_links = list_display
    readonly_fields = ("key", "created_at", "updated_at")
