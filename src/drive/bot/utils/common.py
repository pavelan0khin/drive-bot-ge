from drive.bot.models import Setting


def get_bot_settings() -> Setting:
    return Setting.objects.all().order_by("-id").first()


def notify_about_new_tickets():
    ...
