from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand, UserState
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action
from drive.exam.service import SessionService


@bot.message_handler(commands=[BotCommand.TRANSLATE_ME_BETTER])
@init_action
def translate_me_better_command(action: Action, _):
    action.user.state = UserState.TRANSLATE_ERROR
    bot.send_message(
        action.chat_id,
        _(text.EXPLAIN_TRANSLATION_ERROR),
        reply_markup=action.markup.get_decline_button(),
    )
