from django.db.models import TextChoices


class SessionType(TextChoices):
    EXAM = "exam", "exam"
    TEST = "test", "test"
