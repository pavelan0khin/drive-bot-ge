import os

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from drive.exam.models import TicketImage
from drive.utils.common import progress_bar


class Command(BaseCommand):
    help = "Imports images from a given directory into the ImageModel"

    def add_arguments(self, parser):
        parser.add_argument(
            "dir",
            type=str,
            help="Directory containing the images to import",
            nargs="?",
            default=os.path.join(settings.BASE_DIR, "media/ticket_images/"),
        )

    def handle(self, *args, **kwargs):
        directory = kwargs["dir"]
        all_files = [
            f
            for f in os.listdir(directory)
            if any(f.endswith(ext) for ext in [".jpg", ".png", ".jpeg"])
        ]
        total_files = len(all_files)
        for idx, filename in enumerate(all_files):
            with open(os.path.join(directory, filename), "rb") as image_file:
                file_name = os.path.basename(image_file.name)
                image_instance = TicketImage(image=File(image_file, name=file_name))
                image_instance.save()
                progress_bar(idx + 1, total_files)
        self.stdout.write(self.style.SUCCESS("\nAll images have been imported"))
