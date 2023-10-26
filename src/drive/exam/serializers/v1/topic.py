from rest_framework import serializers

from drive.api.serializers import BaseModelSerializer
from drive.exam import models


class TopicSerializer(BaseModelSerializer):
    name = serializers.CharField(source="name.en")

    class Meta:
        model = models.TicketTopic
        fields = [
            "id",
            "name",
        ]
        translate_fields = ["name"]
