import base64
import os

from django.core.files.storage import default_storage as storage
from PIL import Image

from drive.exam import models


def get_mime_type(image_record: models.TicketImage):
    if image_record.image:
        image = Image.open(image_record.image)
        return Image.MIME.get(image.format)


def download_image(image_record: models.TicketImage, as_base_64: bool = True) -> str | bytes | None:
    if image_record.image:
        images_dir = models.TicketImage._meta.get_field("image").upload_to
        with storage.open(os.path.join(images_dir, image_record.image.name), "rb") as file:
            image_data = file.read()
        if as_base_64:
            image_data = base64.b64encode(image_data).decode("utf-8")
        return image_data
    return None
