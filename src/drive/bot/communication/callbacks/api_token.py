from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.callback_query_handler(func=lambda call: call.data == CallbackData.API_TOKEN)
@init_action
def api_token_call(action: Action, _):
    token = action.user.api_token
    if not token:
        token = action.user.create_api_token()
        message_text = _(text.NEW_API_TOKEN).format(api_token=token.key)
        reply_markup = action.markup.get_back_to_api_button()
    else:
        message_text = _(text.EXISTING_API_TOKEN).format(api_token=token.key)
        reply_markup = action.markup.get_reissue_token_button()
    bot.edit_message_text(
        message_text, action.chat_id, action.message_id, reply_markup=reply_markup
    )
