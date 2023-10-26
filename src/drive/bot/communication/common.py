from drive.bot.communication import text
from drive.bot.conf import Bot
from drive.bot.types import Action
from drive.exam.const import SessionType
from drive.exam.models import Session, Ticket, TicketHistory


def send_ticket(
    action: Action,
    bot: Bot,
    ticket: Ticket,
    ticket_number: int,
    session: Session,
):
    try:
        message_text = ticket.get_as_text(session, ticket_number)
        if ticket.image:
            image = ticket.image.value_to_send()
            message = bot.send_photo(
                action.chat_id,
                image,
                message_text,
                reply_markup=action.markup.get_answers_button(
                    ticket.id, ticket.answers.all(), session.id
                ),
            )
            ticket.image.update_file_id(message.photo[-1].file_id)
        else:
            message = bot.send_message(
                action.chat_id,
                message_text,
                reply_markup=action.markup.get_answers_button(
                    ticket.id, ticket.answers.all(), session.id
                ),
            )
        TicketHistory.objects.create(
            user=action.user.record,
            session=session,
            ticket=ticket,
            bot_message_id=message.id,
        )
    except Exception as error:
        print(error.__class__.__name__, error)


def edit_message_text(
    text: str,
    action: Action,
    bot: Bot,
    ticket: Ticket,
    add_markup: bool,
    session: Session,
):
    if add_markup:
        markup = action.markup.get_answers_button(ticket.id, ticket.answers.all(), session.id)
    else:
        markup = action.markup.get_ticket_description_button(ticket.id)
    if action.is_replied_action_photo:
        bot.edit_message_caption(text, action.chat_id, action.message_id, reply_markup=markup)
    else:
        bot.edit_message_text(text, action.chat_id, action.message_id, reply_markup=markup)


def finish_ticket(
    action: Action,
    bot: Bot,
    ticket: Ticket,
    ticket_number: int,
    chosen_answer_id: int,
    session: Session,
):
    if not action.user.know_about_chosen_ticket:
        action.user.know_about_chosen_ticket = True
        bot.answer_callback_query(
            action.call_id,
            action.gettext(text.WHICH_ANSWER_CHOSEN, action.user.language),
            True,
        )
    message_text = ticket.get_as_text(
        session,
        ticket_number,
        mark_with_color=True,
        chosen_answer=chosen_answer_id,
    )
    edit_message_text(message_text, action, bot, ticket, False, session)
    is_answer_valid = next(
        ans for ans in ticket.answers.all() if ans.id == chosen_answer_id
    ).is_valid
    ticket_history = TicketHistory.objects.get(
        user=action.user.record, session=session, ticket=ticket
    )
    ticket_history.selected_answer_id = chosen_answer_id
    ticket_history.is_valid = is_answer_valid
    ticket_history.save()


def finish_session(action: Action, bot: Bot, session: Session):
    valid_solved_tickets = len(session.valid_solved_tickets.all())
    invalid_solved_tickets = len(session.invalid_solved_tickets.all())
    message_text = action.gettext(text.EXAM_FINISHED, action.user.language).format(
        total_tickets=valid_solved_tickets + invalid_solved_tickets,
        total_valid=valid_solved_tickets,
        total_invalid=invalid_solved_tickets,
    )
    if session.session_type == SessionType.EXAM:
        if invalid_solved_tickets > 3:
            exam_result = action.gettext(text.EXAM_FAILED, action.user.language)
        else:
            exam_result = action.gettext(text.EXAM_PASSED, action.user.language)
        message_text += f"\n\n{exam_result}"
    bot.send_message(action.chat_id, message_text, reply_markup=action.markup.get_main_buttons())
