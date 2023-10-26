from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.message_handler(commands=[BotCommand.LANGUAGE])
@init_action
def language_command(action: Action, _):
    bot.send_message(
        action.chat_id,
        _(text.SELECT_NEW_LANGUAGE),
        reply_markup=action.markup.get_language_buttons(True),
    )
