from typing import List

from telebot import types

from drive.bot.types import Action
from drive.bot.utils.common import get_bot_settings


def should_interact(action: Action) -> bool:
    if action.user.is_blocked:
        return False
    bot_settings = get_bot_settings()
    if not bot_settings.working:
        action.notify_about_not_working_reason(
            bot_settings.not_working_reason.get(action.user.language)
        )
    return bot_settings.working


def init_action(*args, required_state: str | List[str] | None = None):
    if args and callable(args[0]):
        func = args[0]

        def wrapper(original_action: types.Message | types.CallbackQuery):
            action = Action(original_action)
            if should_interact(action):
                translator = action.translations[action.user.language]
                return func(action, translator.gettext)

        return wrapper
    else:

        def decorator(func):
            def wrapper(original_action: types.Message | types.CallbackQuery):
                action = Action(original_action)
                if should_interact(action):
                    if required_state:
                        if isinstance(required_state, str):
                            is_valid = action.user.state.startswith(required_state)
                        else:
                            is_valid = any(
                                action.user.state.startswith(req_state)
                                for req_state in required_state
                            )
                    else:
                        is_valid = True
                    if is_valid:
                        translator = action.translations[action.user.language]
                        return func(action, translator.gettext)
                    else:
                        action.notify_about_wrong_action()

            return wrapper

        return decorator


def ignore_exception_before_migration(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args)
        except Exception:
            return []

    return wrapper
