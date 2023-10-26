from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import CallbackData
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action
from drive.exam.models import TicketProblem


@bot.callback_query_handler(func=lambda call: call.data.startswith(CallbackData.WRITE_ME))
@init_action
def write_me_call(action: Action, _):
    ticket_problem_id = action.call_data_arg
    ticket_problem = TicketProblem.objects.get(id=ticket_problem_id)
    ticket_problem.wants_answer = True
    ticket_problem.save()
    bot.edit_message_reply_markup(action.chat_id, action.message_id)
    bot.answer_callback_query(action.call_id, _(text.WRITE_ME_BUTTON_RESPONSE), True)
