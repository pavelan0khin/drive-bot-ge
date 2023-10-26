from urllib.parse import urljoin

from django.conf import settings

from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.callback_query_handler(func=lambda call: call.data == CallbackData.NEW_API_TOKEN)
@init_action
def new_api_token_call(action: Action, _):
    token = action.user.reissue_api_token()
    message_text = _(text.REISSUED_TOKEN).format(api_token=token.key)
    bot.edit_message_text(
        message_text,
        action.chat_id,
        action.message_id,
        reply_markup=action.markup.get_back_to_api_button(),
    )
