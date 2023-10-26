from django.core.exceptions import ValidationError
from django.db import models


class JSONField(models.JSONField):
    def to_python(self, value):
        data = super().to_python(value)

        required_keys = {"en", "ru", "ka", "az", "tr", "hy", "uk"}
        if not required_keys.issubset(data.keys()):
            missing_keys = required_keys - data.keys()
            raise ValidationError(f"JSON is missing the following keys: {', '.join(missing_keys)}")
        return data
