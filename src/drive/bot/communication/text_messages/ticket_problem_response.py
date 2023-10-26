from django.conf import settings
from telebot.apihelper import ApiTelegramException

from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import ChatType, ContentType
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action
from drive.exam import models


@bot.message_handler(content_types=[ContentType.TEXT], chat_types=[ChatType.SUPERGROUP])
@init_action
def ticket_problem_response_message(action: Action, _):
    if settings.PROBLEMS_CHAT_ID == action.chat_id:
        ticket_problem = models.TicketProblem.objects.get(bot_message_id=action.replied_message_id)
        message_text = action.gettext(
            text.PROBLEM_RESOLVED_MESSAGE, ticket_problem.user.main_language
        ).format(response=action.message_text)
        try:
            bot.send_message(
                ticket_problem.user.telegram_id,
                message_text,
                reply_to_message_id=ticket_problem.user_message_id,
            )
            bot.send_message(action.chat_id, "Done", reply_to_message_id=action.message_id)
        except ApiTelegramException as error:
            bot.send_message(
                action.chat_id,
                f"Error sending message:{error}",
                reply_to_message_id=action.message_id,
            )
