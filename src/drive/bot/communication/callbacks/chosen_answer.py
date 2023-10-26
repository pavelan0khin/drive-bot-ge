from drive.bot.communication import text
from drive.bot.communication.common import finish_session, finish_ticket, send_ticket
from drive.bot.conf import bot
from drive.bot.const import CallbackData, UserState
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action
from drive.exam import models
from drive.exam.service import SessionService


@bot.callback_query_handler(func=lambda call: call.data.startswith(CallbackData.CHOSEN_ANSWER))
@init_action
def chosen_answer_call(action: Action, _):
    session_id = action.user.state_arg
    answer_id, ticket_id, called_session_id = action.call_data_args
    if session_id != called_session_id or session_id is None:
        bot.answer_callback_query(action.call_id, _(text.SESSION_IS_OVER), True)
        return
    ticket = models.Ticket.objects.get(id=ticket_id)
    service = SessionService(action.user)
    is_valid = service.add_answer(session_id, answer_id)
    if action.user.know_about_chosen_ticket:
        is_valid_emoji = {True: "🟢", False: "🔴"}
        bot.answer_callback_query(action.call_id, is_valid_emoji.get(is_valid))
    previous_ticket_number = service.get_current_ticket_count() - 1
    finish_ticket(action, bot, ticket, previous_ticket_number, answer_id, service.session)
    is_finished, new_ticket = service.get_ticket()
    if is_finished:
        action.user.state = UserState.MAIN
        service.finish_session()
        finish_session(action, bot, service.session)
    else:
        ticket_number = service.get_current_ticket_count()
        send_ticket(action, bot, new_ticket, ticket_number, service.session)
