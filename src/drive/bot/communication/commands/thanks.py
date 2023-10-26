from drive.bot.communication import text
from drive.bot.conf import bot
from drive.bot.const import BotCommand
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action


@bot.message_handler(commands=[BotCommand.THANKS])
@init_action
def thanks_command(action: Action, _):
    requisites = (
        "<b>Bank Of Georgia</b>:\n\n"
        "Account Number: <code>GE44BG0000000537911384</code>\n\n"
        "<b>TBC</b>:\n\n"
        "Account number: <code>GE11TB7126945064400003</code>\n\n"
        "<b>Crypto</b>:\n\n"
        "USDT TRC20: <code>TDS3DYJYZJ8D1uwQrtLxQrJ9yokuQDvAmi</code>\n\n"
        "BTC: <code>bc1q6yhdcehgq8xnjkxx8c33ulcr8czahctwskqgjz</code>\n\n"
        "Ethereum: <code>0xE5827528FFf4c248A3d8bB35A2aAF9863c434Ca6</code>"
    )
    message_text = _(text.DONATE_MESSAGE).format(requisites=requisites)
    bot.send_message(action.chat_id, message_text)
