import warnings

from django.db.models import TextChoices
from telebot import types


class BotCommand:
    START = "start"
    ABOUT = "about"
    LANGUAGE = "language"
    NOTIFICATIONS = "notifications"
    CLEAR_HISTORY = "clearhistory"
    PROBLEM = "problem"
    API = "api"
    THANKS = "thanks"
    TRANSLATE_ME_BETTER = "translatemebetter"

    @classmethod
    def as_telegram_commands(cls) -> list[types.BotCommand]:
        attributes = [
            attr
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith("__")
        ]
        commands = [
            types.BotCommand(cls.START, "Start"),
            types.BotCommand(cls.API, description="About"),
            types.BotCommand(cls.LANGUAGE, description="Change language"),
            types.BotCommand(cls.NOTIFICATIONS, description="Turn on/off notifications"),
            types.BotCommand(cls.CLEAR_HISTORY, description="Clear tickets history"),
            types.BotCommand(cls.PROBLEM, description="Report ticket problem"),
            types.BotCommand(cls.API, description="API Info"),
            types.BotCommand(cls.THANKS, description="Say thanks :)"),
            types.BotCommand(cls.TRANSLATE_ME_BETTER, description="Translation problem"),
        ]
        if len(attributes) != len(commands):
            warnings.warn(
                "Add missing commands to the '.as_telegram_commands(cls)' "
                "method of the BotCommand class!",
                category=UserWarning,
            )
        return commands


class ContentType:
    TEXT = "text"


class ChatType:
    SUPERGROUP = "supergroup"


class UserState:
    NEW_USER = "new_user"
    ALLOW_NOTIFICATIONS = "allow_notifications"
    MAIN = "main"
    CHOOSING_CATEGORY = "choosing_category"
    EXAM_IN_PROGRESS = "exam_in_progress"
    TICKET_PROBLEM = "ticket_problem"
    TRANSLATE_ERROR = "translate_error"


class Language(TextChoices):
    ENGLISH = (
        "en",
        "English",
    )
    RUSSIAN = "ru", "Russian"
    GEORGIAN = "ka", "Georgian"
    UKRAINIAN = "uk", "Ukrainian"
    AZERBAIJANI = "az", "Azerbaijani"
    ARMENIAN = "hy", "Armenian"
    TURKISH = "tr", "Turkish"

    @classmethod
    def supported_languages(cls) -> list:
        return [choice[0] for choice in cls.choices]

    @classmethod
    def get_initial_json(cls) -> dict:
        return {k[0]: "" for k in cls.choices}


class CallbackData:
    CHOSEN_LANGUAGE = "chosen_language"
    CHANGED_LANGUAGE = "changed_language"
    ALLOW_NOTIFICATIONS = "allow_notifications"
    CHOSEN_ANSWER = "chosen_answer"
    CLEAR_HISTORY = "clear_history"
    HTTP_REST = "http_rest"
    GRPC = "grpc"
    API_TOKEN = "api_token"
    API_INFO = "api_info"
    NEW_API_TOKEN = "new_api_token"
    WRITE_ME = "write_me"
    TICKET_RESOLVED = "ticket_resolved"


class TelegramErrorDescription:
    MEDIA_CAPTION_TOO_LONG = "MEDIA_CAPTION_TOO_LONG"
