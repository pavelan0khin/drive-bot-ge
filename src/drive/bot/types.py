from django.db.models import Q
from telebot import types

from drive.bot import models
from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import UserState
from drive.bot.i18n import service
from drive.bot.utils.markup import Markup
from drive.exam.service import SessionService


class User:
    def __init__(self, user: types.User):
        self._user = user
        self.record, self.is_new = self._init_database_user()
        if not self.is_new:
            self._update_user_fields()
        else:
            self.state = UserState.NEW_USER

    def _update_user_fields(self):
        lookup_fields = ["username", "first_name", "last_name"]
        updated_fields = []
        for field in lookup_fields:
            old_value = getattr(self.record, field)
            new_value = getattr(self, field)
            if old_value != new_value:
                setattr(self.record, field, new_value)
                updated_fields.append({field: {"old_value": old_value, "new_value": new_value}})
        if updated_fields:
            self.record.save()
            models.UserUpdate.objects.create(user=self.record, updates=updated_fields)

    def _init_database_user(self) -> tuple[models.User, bool]:
        instance, created = models.User.objects.get_or_create(
            telegram_id=self.telegram_id,
            defaults={
                "username": self.username,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "language_code": self._user.language_code,
            },
        )
        return instance, created

    @property
    def telegram_id(self):
        return self._user.id

    @property
    def username(self):
        return self._user.username

    @property
    def first_name(self):
        return self._user.first_name

    @property
    def last_name(self):
        return self._user.last_name

    @property
    def state(self) -> str:
        instance = models.State.objects.filter(user=self.record).order_by("-id").first()
        return instance.state

    @property
    def clean_state(self) -> str:
        state = self.state
        if ":" in state:
            state = state.split(":")[0]
        return state

    @property
    def state_arg(self) -> str | int | None:
        if ":" not in self.state:
            return None
        arg = self.state.split(":")[1]
        if arg.isnumeric():
            return int(arg)
        return arg

    @state.setter
    def state(self, value: str):
        models.State.objects.create(user=self.record, state=value)

    @property
    def language(self) -> str:
        return self.record.main_language

    @language.setter
    def language(self, value: str):
        self.record.main_language = value
        self.record.save()

    @property
    def wants_notification(self) -> bool:
        return self.record.wants_notifications

    @wants_notification.setter
    def wants_notification(self, value: bool):
        self.record.wants_notifications = value
        self.record.save()

    @property
    def know_about_chosen_ticket(self) -> bool:
        return self.record.know_about_chosen_answer

    @know_about_chosen_ticket.setter
    def know_about_chosen_ticket(self, value: bool):
        self.record.know_about_chosen_answer = value
        self.record.save()

    @property
    def is_blocked(self) -> bool:
        return self.record.is_blocked

    @property
    def previous_state(self) -> str:
        state = (
            models.State.objects.filter(
                ~(
                    Q(state__icontains=UserState.TRANSLATE_ERROR)
                    | Q(state__icontains=UserState.TICKET_PROBLEM)
                )
            )
            .order_by("-created_at")
            .first()
        )
        return state.state

    @property
    def readable_name(self) -> str:
        if self.last_name:
            name = f"{self.first_name} {self.last_name}"
        else:
            name = f"{self.first_name}"
        if self.username:
            name += f" | @{self.username}"
        return name

    @property
    def api_token(self) -> models.APIToken | None:
        if hasattr(self.record, "auth_token"):
            return self.record.auth_token

    def delete_token(self) -> None:
        token = self.api_token
        token.delete()

    def reissue_api_token(self) -> models.APIToken:
        self.delete_token()
        return self.create_api_token()

    def set_previous_state(self):
        self.state = self.previous_state

    def create_api_token(self) -> models.APIToken:
        token = models.APIToken.objects.create(user=self.record)
        return token


class Action:
    def __init__(self, action: types.Message | types.CallbackQuery):
        self._action = action
        self.user = User(action.from_user)
        self.markup = Markup(self.user.language, self.gettext)

    @property
    def is_replied_action_photo(self):
        if isinstance(self._action, types.CallbackQuery):
            return self._action.message.caption is not None
        return False

    @property
    def text_entities(self) -> list[types.MessageEntity] | None:
        if self._action.message.caption_entities:
            return self._action.message.caption_entities
        elif self._action.message.entities:
            return self._action.message.entities
        return None

    @property
    def chat_id(self) -> int:
        if isinstance(self._action, types.Message):
            return self._action.chat.id
        return self._action.message.chat.id

    @property
    def message_id(self) -> int:
        if isinstance(self._action, types.Message):
            return self._action.id
        return self._action.message.id

    @property
    def message_text(self) -> str:
        if isinstance(self._action, types.Message):
            return self._action.text
        if self.is_replied_action_photo:
            return self._action.message.caption
        return self._action.message.text

    @property
    def call_id(self) -> int | None:
        if isinstance(self._action, types.CallbackQuery):
            return self._action.id
        return None

    @property
    def call_data_raw(self) -> str:
        if isinstance(self._action, types.CallbackQuery):
            return self._action.data

    @property
    def call_data_arg(self) -> str | int:
        arg = self.call_data_raw.split(":")[1]
        if arg.isnumeric():
            return int(arg)
        return arg

    @property
    def call_data_args(self) -> list[str | int]:
        args = []
        raw_args = self.call_data_raw.split(":")[1:]
        for arg in raw_args:
            if arg.isnumeric():
                args.append(int(arg))
            else:
                args.append(arg)
        return args

    @property
    def translations(self):
        return service.translations()

    @staticmethod
    def gettext(text: str, language: str):
        return service.gettext(text, language)

    @property
    def replied_message_id(self) -> int | None:
        if self._action.reply_to_message:
            return self._action.reply_to_message.id
        return None

    def notify_about_wrong_action(self):
        bot.send_message(self.chat_id, self.gettext(text.UNKNOWN_ACTION, self.user.language))

    def notify_about_not_working_reason(self, message: str):
        bot.send_message(self.chat_id, message)

    def test(self):
        bot.set_my_commands()

    def resolve_previous_state(self):
        self.user.state = self.user.previous_state
        if self.user.clean_state in [UserState.CHOOSING_CATEGORY, UserState.EXAM_IN_PROGRESS]:
            if self.user.clean_state == UserState.CHOOSING_CATEGORY:
                reply_markup = self.markup.get_category_buttons()
                message_text = self.gettext(text.SELECT_CATEGORY, self.user.language)
                reply_to_message_id = None
            else:
                service = SessionService(self.user.record)
                reply_markup = self.markup.get_decline_button()
                message_text = self.gettext(text.CONTINUE_EXAM, self.user.language)
                reply_to_message_id = service.get_last_bot_message_id(self.user.state_arg)
        else:
            reply_markup = self.markup.get_main_buttons()
            message_text = self.gettext(text.SELECT_BUTTONS, self.user.language)
            reply_to_message_id = None
        bot.send_message(
            self.chat_id,
            message_text,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )
