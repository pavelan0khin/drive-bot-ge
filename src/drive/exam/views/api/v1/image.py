from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin

from drive.exam import models
from drive.exam.serializers.v1 import ImageSerializer


class ImageViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.TicketImage.objects.all().order_by("id")
    serializer_class = ImageSerializer
