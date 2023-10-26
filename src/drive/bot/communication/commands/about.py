from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.message_handler(commands=[BotCommand.ABOUT])
@init_action
def about_command(action: Action, _):
    bot.send_message(action.chat_id, _(text.ABOUT_MESSAGE))
