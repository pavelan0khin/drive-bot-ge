from typing import Callable

from drive.bot.conf import bot
from drive.bot.const import ContentType, UserState
from drive.bot.types import Action
from drive.bot.utils.decorator import init_action

from . import ticket_problem_response
from .ticket_problem import ticket_problem_message
from .translate_error import translate_error_message


@bot.message_handler(content_types=[ContentType.TEXT])
@init_action(required_state=[UserState.TICKET_PROBLEM, UserState.TRANSLATE_ERROR])
def text_message(action: Action, _):
    mapping = {
        UserState.TICKET_PROBLEM: ticket_problem_message,
        UserState.TRANSLATE_ERROR: translate_error_message,
    }
    original_state = action.user.clean_state
    function: Callable = mapping.get(original_state)
    return function(action, _)
