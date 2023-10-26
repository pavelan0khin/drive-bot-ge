class ExamException(Exception):
    ...


class NoTicketsAvailableException(ExamException):
    ...


class TicketParsingException(Exception):
    ...
