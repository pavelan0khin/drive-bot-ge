from django.conf import settings

from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import UserState
from drive.bot.types import Action
from drive.exam import models
from drive.exam.service import SessionService


def ticket_problem_message(action: Action, _):
    if len(action.message_text) > 3500:
        bot.send_message(action.chat_id, _(text.MESSAGE_TOO_LONG))
        return
    ticket_id = action.user.state_arg
    message_text = (
        f"Problem with ticket #{ticket_id}\n"
        f"Author: {action.user.readable_name}\n"
        f"Telegram ID: {action.user.telegram_id}\n"
        f"Message:\n\n«{action.message_text}»"
    )
    ticket_problem = models.TicketProblem.objects.create(
        user=action.user.record,
        ticket_id=ticket_id,
        user_message_id=action.message_id,
        text=action.message_text,
    )
    message = bot.send_message(
        settings.PROBLEMS_CHAT_ID,
        message_text,
        reply_markup=action.markup.get_problem_tickets_button(ticket_id, ticket_problem.id),
    )
    ticket_problem.bot_message_id = message.id
    ticket_problem.save()
    bot.send_message(
        action.chat_id,
        _(text.PROBLEM_IN_PROGRESS),
        reply_markup=action.markup.get_notify_me_button(ticket_problem.id),
    )
    action.resolve_previous_state()
