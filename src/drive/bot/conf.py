from typing import Callable, List, Optional

from django.conf import settings
from telebot import TeleBot

from drive.bot.const import BotCommand


class Bot(TeleBot):
    def __init__(self, token: str):
        super().__init__(
            token=token,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )

    def message_handler(
        self,
        commands: Optional[List[str]] = None,
        regexp: Optional[str] = None,
        func: Optional[Callable] = None,
        content_types: Optional[List[str]] = None,
        chat_types: Optional[List[str]] = None,
        **kwargs,
    ):
        return super().message_handler(commands, regexp, func, content_types, chat_types, **kwargs)

    def callback_query_handler(self, func, **kwargs):
        return super().callback_query_handler(func, **kwargs)


bot = Bot(settings.TELEGRAM_BOT_TOKEN)

bot.set_my_commands(BotCommand.as_telegram_commands())
