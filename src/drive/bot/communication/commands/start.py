from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.message_handler(commands=[BotCommand.START])
@init_action
def start_command(action: Action, _):
    if action.user.is_new:
        bot.send_message(
            action.chat_id,
            _(text.NEW_USER_START_MESSAGE),
            reply_markup=action.markup.get_language_buttons(),
        )
    else:
        bot.send_message(
            action.chat_id,
            _(text.START_MESSAGE),
            reply_markup=action.markup.get_main_buttons(),
        )
