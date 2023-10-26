from django.contrib import admin
from django.db.models.fields.json import JSONField
from jsoneditor.forms import JSONEditor


class BaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {
            "widget": JSONEditor(
                init_options={
                    "mode": "code",
                    "modes": [
                        "view",
                        "code",
                    ],
                },
                ace_options={"readOnly": False},
            )
        }
    }

    readonly_fields = ("created_at", "updated_at")

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, JSONField):
            if request.resolver_match.url_name.endswith("_add"):
                widget = JSONEditor(
                    init_options={
                        "mode": "code",
                        "modes": ["view", "code"],
                    },
                    ace_options={"readOnly": False},
                )
            else:
                widget = JSONEditor(
                    init_options={
                        "mode": "view",
                        "modes": ["view", "code"],
                    },
                    ace_options={"readOnly": False},
                )
            return db_field.formfield(widget=widget)

        return super().formfield_for_dbfield(db_field, request, **kwargs)
