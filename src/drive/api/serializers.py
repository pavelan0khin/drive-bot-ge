from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request", None)
        if request:
            lang = request.query_params.get("lang", request.user.main_language)
            for field_name in self.Meta.translate_fields:
                field = getattr(instance, field_name)
                if field and isinstance(field, dict):
                    representation[field_name] = field.get(lang)
        return representation
