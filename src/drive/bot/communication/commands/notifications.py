from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.message_handler(commands=[BotCommand.NOTIFICATIONS])
@init_action
def notifications_command(action: Action, _):
    action.user.wants_notification = not action.user.wants_notification
    if action.user.wants_notification:
        message_text = _(text.NOTIFICATIONS_ARE_OFF)
    else:
        message_text = _(text.NOTIFICATIONS_ARE_ON)
    bot.send_message(action.chat_id, message_text)
