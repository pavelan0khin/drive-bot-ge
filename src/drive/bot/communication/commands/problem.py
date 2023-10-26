from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand, UserState
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action
from drive.exam.models import TicketHistory


@bot.message_handler(commands=[BotCommand.PROBLEM])
@init_action
def problem_command(action: Action, _):
    replied_message_id = action.replied_message_id
    ticket_history = TicketHistory.objects.filter(
        user=action.user.record, bot_message_id=replied_message_id
    )
    if not ticket_history:
        bot.send_message(action.chat_id, _(text.REPLY_BOT_MESSAGE))
        return
    action.user.state = f"{UserState.TICKET_PROBLEM}:{ticket_history.first().ticket.id}"
    bot.send_message(
        action.chat_id,
        _(text.DESCRIBE_YOUR_PROBLEM),
        reply_markup=action.markup.get_decline_button(),
    )
