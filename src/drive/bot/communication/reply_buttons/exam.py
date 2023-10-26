from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import Language, UserState
from drive.bot.i18n.service import gettext
from drive.bot.types import Action
from drive.bot.utils.decorator import ignore_exception_before_migration, init_action
from drive.exam.const import SessionType
from drive.exam.service import SessionService
from drive.exam.service.exceptions import NoTicketsAvailableException


@ignore_exception_before_migration
def get_test_buttons(test_type: str) -> list:
    return [gettext(test_type, lang) for lang in Language.supported_languages()]


exam_buttons = get_test_buttons(text.EXAM)
all_tests_buttons = get_test_buttons(text.ALL_TICKETS)


test_buttons = exam_buttons + all_tests_buttons


@bot.message_handler(func=lambda message: message.text in test_buttons)
@init_action
def exam_button(action: Action, _):
    session_type = SessionType.EXAM if action.message_text in exam_buttons else SessionType.TEST
    service = SessionService(action.user.record)
    try:
        session = service.start_session(session_type)
    except NoTicketsAvailableException:
        action.user.state = UserState.MAIN
        bot.send_message(action.chat_id, _(text.DROP_PASSED_TICKETS_HISTORY))
    else:
        action.user.state = f"{UserState.CHOOSING_CATEGORY}:{session.id}"
        bot.send_message(
            action.chat_id,
            _(text.SELECT_CATEGORY),
            reply_markup=action.markup.get_category_buttons(),
        )
