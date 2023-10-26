from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action
from drive.exam import models


@bot.callback_query_handler(func=lambda call: call.data.startswith(CallbackData.TICKET_RESOLVED))
@init_action
def ticket_resolved_call(action: Action, _):
    ticket_problem_id = action.call_data_arg
    ticket_problem = models.TicketProblem.objects.get(id=ticket_problem_id)
    ticket_problem.is_resolved = True
    ticket_problem.save()
    bot.edit_message_text("🟢 Resolved\n" + action.message_text, action.chat_id, action.message_id)
