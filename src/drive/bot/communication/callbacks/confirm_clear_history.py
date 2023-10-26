from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action, UserState
from drive.bot.utils.decorator import init_action
from drive.exam.service import SessionService


@bot.callback_query_handler(func=lambda call: call.data.startswith(CallbackData.CLEAR_HISTORY))
@init_action
def confirm_clear_history_call(action: Action, _):
    clear_history = bool(action.call_data_arg)
    if clear_history:
        action.user.state = UserState.MAIN
        service = SessionService(action.user.record)
        service.clear_history()
        message_text = _(text.HISTORY_IS_CLEAR)
    else:
        message_text = _(text.HISTORY_IS_NOT_CLEAR)
    bot.edit_message_reply_markup(action.chat_id, action.message_id)
    bot.send_message(action.chat_id, message_text, reply_markup=action.markup.get_main_buttons())
