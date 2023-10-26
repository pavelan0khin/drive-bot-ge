from rest_framework import serializers

from drive.api.serializers import BaseModelSerializer
from drive.exam import models


class CategorySerializer(BaseModelSerializer):
    name = serializers.CharField(source="name.en")
    description = serializers.CharField(source="description.en")

    class Meta:
        model = models.TicketCategory
        fields = [
            "id",
            "name",
            "description",
        ]
        translate_fields = ["name", "description"]
