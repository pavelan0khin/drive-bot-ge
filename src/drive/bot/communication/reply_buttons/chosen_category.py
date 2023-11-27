from drive.bot.communication import text
from drive.bot.communication.common import send_ticket
from drive.bot.conf import bot
from drive.bot.const import Language, UserState
from drive.bot.types import Action
from drive.bot.utils.decorator import ignore_exception_before_migration, init_action
from drive.exam import models
from drive.exam.service import SessionService


@ignore_exception_before_migration
def get_categories() -> list:
    return list(
        {
            cat.name.get(lang)
            for lang in Language.supported_languages()
            for cat in models.TicketCategory.objects.all()
        }
    )


category_buttons = get_categories()


@bot.message_handler(func=lambda message: message.text in category_buttons)
@init_action(required_state=UserState.CHOOSING_CATEGORY)
def chosen_category_button(action: Action, _):
    session_id = action.user.state_arg
    session = models.Session.objects.get(id=session_id)
    category = models.TicketCategory.objects.get(
        name__contains={action.user.language: action.message_text}
    )
    session.add_category(category)
    service = SessionService.from_session_id(action.user.record, session_id)
    service.reload_tickets_with_category()
    action.user.state = f"{UserState.EXAM_IN_PROGRESS}:{session.id}"
    bot.send_message(
        action.chat_id,
        _(text.EXAM_STARTED),
        reply_markup=action.markup.get_decline_button(),
    )
    _, ticket = service.get_ticket(session)
    ticket_number = service.get_current_ticket_count()
    send_ticket(action, bot, ticket, ticket_number, session)
