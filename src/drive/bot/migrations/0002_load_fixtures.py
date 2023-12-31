# Generated by Django 4.2.6 on 2023-10-24 09:08

import sys
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import OutputWrapper
from django.db import migrations


def load_fixtures(_, __):
    fixture = "settings_fixture.json"
    fixtures_path = Path(settings.BASE_DIR, f"bot/migrations/fixtures/{fixture}")
    call_command("loaddata", fixtures_path, app_label="exam")


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0001_initial"),
    ]

    operations = [migrations.RunPython(load_fixtures, reverse_code=migrations.RunPython.noop)]
