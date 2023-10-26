from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.callback_query_handler(func=lambda call: call.data == CallbackData.API_INFO)
@init_action
def api_info_call(action: Action, _):
    bot.edit_message_text(
        _(text.API_COMMAND_RESPONSE),
        action.chat_id,
        action.message_id,
        reply_markup=action.markup.get_api_buttons(),
    )
