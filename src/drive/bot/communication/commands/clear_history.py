from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.message_handler(commands=[BotCommand.CLEAR_HISTORY])
@init_action
def clear_history_command(action: Action, _):
    bot.send_message(
        action.chat_id,
        _(text.CONFIRM_CLEAR_HISTORY),
        reply_markup=action.markup.get_confirm_clear_history_buttons(),
    )
