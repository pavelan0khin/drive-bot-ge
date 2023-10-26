from django.conf import settings

from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import UserState
from drive.bot.types import Action
from drive.exam import models
from drive.exam.service import SessionService


def translate_error_message(action: Action, _):
    if len(action.message_text) > 3500:
        bot.send_message(action.chat_id, _(text.MESSAGE_TOO_LONG))
        return
    message_text = (
        f"Translation error\n"
        f"Author: {action.user.readable_name}\n"
        f"Telegram ID: {action.user.telegram_id}\n"
        f"Language: {action.user.language}\n"
        f"Message:\n\n«{action.message_text}»"
    )
    bot.send_message(settings.PROBLEMS_CHAT_ID, message_text)
    bot.send_message(action.chat_id, _(text.TRANSLATION_PROBLEM_IN_PROGRESS))
    action.resolve_previous_state()
