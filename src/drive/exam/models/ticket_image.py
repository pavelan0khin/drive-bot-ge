import io

from django.db import models

from drive.utils.models import BaseModel


class TicketImage(BaseModel):
    image = models.ImageField(verbose_name="Image", upload_to="ticket_images/")
    file_id = models.CharField(max_length=1024, verbose_name="File ID", null=True, blank=True)

    class Meta:
        verbose_name = "Ticket Image"
        verbose_name_plural = "Ticket Images"

    def __str__(self):
        return self.image.name

    def value_to_send(self) -> str | io.BufferedReader:
        from drive.exam.utils import download_image

        if self.file_id:
            return self.file_id
        image = download_image(self, False)
        return image

    def update_file_id(self, file_id: str):
        self.file_id = file_id
        self.save()
