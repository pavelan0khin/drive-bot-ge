import base64

from django.core.files.storage import default_storage as storage
from PIL import Image
from rest_framework import serializers

from drive.exam import models
from drive.exam.utils import download_image, get_mime_type


class ImageSerializer(serializers.ModelSerializer):
    image_base64 = serializers.SerializerMethodField("get_image_as_base64")
    mime_type = serializers.SerializerMethodField("get_mime_type")

    @staticmethod
    def get_image_as_base64(obj) -> str:
        return download_image(obj, True) or ""

    @staticmethod
    def get_mime_type(obj) -> str:
        return get_mime_type(obj) or ""

    class Meta:
        model = models.TicketImage
        fields = ["id", "image_base64", "mime_type"]
