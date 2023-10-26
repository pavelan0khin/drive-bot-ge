from rest_framework import serializers

from drive.api.serializers import BaseModelSerializer
from drive.exam import models


class AnswerSerializer(BaseModelSerializer):
    answer = serializers.CharField(source="answer.en")
    ticket_id = serializers.PrimaryKeyRelatedField(
        source="ticket", queryset=models.Ticket.objects.all()
    )

    class Meta:
        model = models.Answer
        fields = ["id", "ticket_id", "answer", "is_valid"]
        translate_fields = ["answer"]
