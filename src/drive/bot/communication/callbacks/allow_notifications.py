from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action, UserState
from drive.bot.utils.decorator import init_action


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(CallbackData.ALLOW_NOTIFICATIONS)
)
@init_action
def allow_notifications_call(action: Action, _):
    action.user.state = UserState.MAIN
    wants_notifications = bool(int(action.call_data_arg))
    action.user.wants_notification = wants_notifications
    if wants_notifications:
        message_text = _(text.NOTIFICATIONS_ARE_ON)
    else:
        message_text = _(text.NOTIFICATIONS_ARE_OFF)
    bot.edit_message_text(message_text, action.chat_id, action.message_id)
    bot.send_message(
        action.chat_id,
        _(text.SELECT_BUTTONS),
        reply_markup=action.markup.get_main_buttons(),
    )
