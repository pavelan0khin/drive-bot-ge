from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import Language, UserState
from drive.bot.i18n.service import gettext
from drive.bot.types import Action
from drive.bot.utils.decorator import ignore_exception_before_migration, init_action
from drive.exam.service import SessionService


@ignore_exception_before_migration
def get_decline_buttons() -> list:
    return [gettext(text.DECLINE, lang) for lang in Language.supported_languages()]


decline_buttons = get_decline_buttons()


@bot.message_handler(func=lambda message: message.text in decline_buttons)
@init_action(
    required_state=[
        UserState.EXAM_IN_PROGRESS,
        UserState.CHOOSING_CATEGORY,
        UserState.TICKET_PROBLEM,
        UserState.TRANSLATE_ERROR,
    ]
)
def decline_button(action: Action, _):
    exam_states = [UserState.EXAM_IN_PROGRESS, UserState.CHOOSING_CATEGORY]
    service = SessionService(action.user.record)
    reply_to_message_id = None
    if action.user.clean_state in exam_states:
        action.user.state = UserState.MAIN
        service.decline_last_session()
        message_text = _(text.ACTION_DECLINED)
        reply_markup = action.markup.get_main_buttons()
    else:
        action.user.set_previous_state()
        if action.user.previous_state.startswith(UserState.EXAM_IN_PROGRESS):
            reply_to_message_id = service.get_last_bot_message_id(action.user.state_arg)
            message_text = _(text.CONTINUE_EXAM)
            reply_markup = action.markup.get_decline_button()
        elif action.user.previous_state.startswith(UserState.CHOOSING_CATEGORY):
            message_text = _(text.SELECT_CATEGORY)
            reply_markup = action.markup.get_category_buttons()
        else:
            message_text = _(text.ACTION_DECLINED)
            reply_markup = action.markup.get_main_buttons()
    bot.send_message(
        action.chat_id,
        message_text,
        reply_markup=reply_markup,
        reply_to_message_id=reply_to_message_id,
    )
