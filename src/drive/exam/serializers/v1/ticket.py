from rest_framework import serializers

from drive.api.serializers import BaseModelSerializer
from drive.exam import models


class TicketSerializer(BaseModelSerializer):
    question = serializers.CharField(source="question.en")
    description = serializers.CharField(source="description.en")
    image_id = serializers.PrimaryKeyRelatedField(
        source="image", queryset=models.TicketImage.objects.all()
    )
    topic_id = serializers.PrimaryKeyRelatedField(
        source="topic", queryset=models.TicketTopic.objects.all()
    )
    categories_ids = serializers.PrimaryKeyRelatedField(
        source="categories", queryset=models.TicketCategory.objects.all(), many=True
    )

    class Meta:
        model = models.Ticket
        fields = [
            "id",
            "external_id",
            "question",
            "image_id",
            "description",
            "topic_id",
            "categories_ids",
        ]
        translate_fields = ["question", "description"]
