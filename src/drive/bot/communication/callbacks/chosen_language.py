from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action, UserState
from drive.bot.utils.decorator import init_action
from drive.bot.utils.markup import Markup


@bot.callback_query_handler(func=lambda call: call.data.startswith(CallbackData.CHOSEN_LANGUAGE))
@init_action
def chosen_language_call(action: Action, _):
    language_code = action.call_data_arg
    action.markup = Markup(language_code, action.gettext)
    action.user.language = language_code

    bot.edit_message_text(
        action.gettext(text.LANGUAGE_SELECTED, language_code),
        action.chat_id,
        action.message_id,
    )
    action.user.state = UserState.ALLOW_NOTIFICATIONS
    bot.send_message(
        action.chat_id,
        action.gettext(text.ALLOW_NOTIFICATIONS, language_code),
        reply_markup=action.markup.get_allow_notification_buttons(),
    )
