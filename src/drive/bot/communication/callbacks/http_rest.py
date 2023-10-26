from urllib.parse import urljoin

from django.conf import settings

from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.callback_query_handler(func=lambda call: call.data == CallbackData.HTTP_REST)
@init_action
def http_rest_call(action: Action, _):
    message_text = _(text.HTTP_REST_INFO).format(
        openapi_url=urljoin(settings.PROJECT_URL, "api/v1/openapi/"),
        redoc_url=urljoin(settings.PROJECT_URL, "api/v1/redoc/"),
    )
    bot.edit_message_text(
        message_text,
        action.chat_id,
        action.message_id,
        reply_markup=action.markup.get_back_to_api_button(),
    )
