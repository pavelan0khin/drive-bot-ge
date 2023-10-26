from urllib.parse import urljoin

from django.conf import settings
from telebot import types

from drive.bot.communication import text
from drive.bot.const import CallbackData
from drive.exam import models as exam_models


class Markup:
    def __init__(self, language: str, gettext):
        self.language = language
        self._ = gettext
        self.gettext = gettext

    @staticmethod
    def get_language_buttons(changing: bool = False) -> types.InlineKeyboardMarkup:
        if changing:
            callback_data = CallbackData.CHANGED_LANGUAGE
        else:
            callback_data = CallbackData.CHOSEN_LANGUAGE
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        languages = {
            "ru": "Русский 🇷🇺",
            "en": "English 🇬🇧",
            "uk": "Українська 🇺🇦",
            "ka": "ქართული 🇬🇪",
            "hy": "Հայոց 🇦🇲",
            "tr": "Türk 🇹🇷",
            "az": "Azərbaycan 🇦🇿",
        }
        for key, value in languages.items():
            buttons.append(
                types.InlineKeyboardButton(value, callback_data=f"{callback_data}:{key}")
            )
        markup.add(*buttons)
        return markup

    def get_decline_button(self) -> types.ReplyKeyboardMarkup:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(self._(text.DECLINE, self.language))
        return markup

    @staticmethod
    def _extract_text_from_reply_markup(
        markup: types.ReplyKeyboardMarkup,
    ) -> str:
        return markup.keyboard[0][0]["text"]  # noqa

    def get_allow_notification_buttons(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(
                self._(text.YES, self.language),
                callback_data=f"{CallbackData.ALLOW_NOTIFICATIONS}:1",
            ),
            types.InlineKeyboardButton(
                self._(text.NO, self.language),
                callback_data=f"{CallbackData.ALLOW_NOTIFICATIONS}:0",
            ),
        )
        return markup

    def get_main_buttons(self) -> types.ReplyKeyboardMarkup:
        buttons = [
            self._(text.EXAM, self.language),
            self._(text.ALL_TICKETS, self.language),
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(*buttons)
        return markup

    def get_category_buttons(self) -> types.ReplyKeyboardMarkup:
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        categories = exam_models.TicketCategory.objects.all()
        buttons = [cat.name.get(self.language) for cat in categories]
        markup.add(*buttons)
        decline_button = self._extract_text_from_reply_markup(self.get_decline_button())
        markup.add(decline_button)
        return markup

    def get_answers_button(
        self,
        ticket_id: int,
        answers: list[exam_models.Answer],
        session_id: int,
    ) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton(
                str(i + 1),
                callback_data=f"{CallbackData.CHOSEN_ANSWER}:{ans.id}:{ticket_id}:{session_id}",
            )
            for i, ans in enumerate(answers)
        ]
        markup.add(*buttons)
        description_url = urljoin(
            settings.PROJECT_URL,
            f"exam/ticket/{ticket_id}/description/{self.language}/",
        )
        markup.add(types.InlineKeyboardButton("❔", url=description_url))
        return markup

    def get_ticket_description_button(self, ticket_id: int) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        description_url = urljoin(
            settings.PROJECT_URL,
            f"exam/ticket/{ticket_id}/description/{self.language}/",
        )
        markup.add(types.InlineKeyboardButton("❔", url=description_url))
        return markup

    def get_confirm_clear_history_buttons(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(
                self._(text.YES, self.language),
                callback_data=f"{CallbackData.CLEAR_HISTORY}:1",
            ),
            types.InlineKeyboardButton(
                self._(text.NO, self.language),
                callback_data=f"{CallbackData.CLEAR_HISTORY}:0",
            ),
        )
        return markup

    @staticmethod
    def get_api_buttons() -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("HTTP REST", callback_data=CallbackData.HTTP_REST),
            types.InlineKeyboardButton("GRPC", callback_data=CallbackData.GRPC),
            types.InlineKeyboardButton("API Token", callback_data=CallbackData.API_TOKEN),
        ]
        markup.add(*buttons)
        return markup

    @staticmethod
    def get_back_to_api_button() -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("⬅️", callback_data=CallbackData.API_INFO))
        return markup

    def get_reissue_token_button(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=1)
        buttons = [
            types.InlineKeyboardButton(
                self._(text.GENERATE_NEW_TOKEN, self.language),
                callback_data=CallbackData.NEW_API_TOKEN,
            ),
            types.InlineKeyboardButton("⬅️", callback_data=CallbackData.API_INFO),
        ]
        markup.add(*buttons)
        return markup

    @staticmethod
    def get_problem_tickets_button(
        ticket_id: int, ticket_problem_id: int
    ) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup()
        ticket_url = urljoin(settings.PROJECT_URL, f"admin/exam/ticket/{ticket_id}/")
        markup.add(
            types.InlineKeyboardButton("View ticket", url=ticket_url),
            types.InlineKeyboardButton(
                "Resolved", callback_data=f"{CallbackData.TICKET_RESOLVED}:{ticket_problem_id}"
            ),
        )
        return markup

    def get_notify_me_button(self, ticket_problem_id: int) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton(
                self._(text.WRITE_ME_BUTTON, self.language),
                callback_data=f"{CallbackData.WRITE_ME}:{ticket_problem_id}",
            )
        )
        return markup
