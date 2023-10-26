import random

from django.db.models import QuerySet
from django.utils import timezone

from drive.bot import models
from drive.exam.const import SessionType
from drive.exam.models import Answer, Session, Ticket, TicketHistory, TicketTopic
from drive.exam.service.exceptions import NoTicketsAvailableException


class SessionService:
    def __init__(self, user: models.User, session: Session | None = None):
        self.user = user
        self.session = session

    @classmethod
    def from_session_id(cls, user: models.User, session_id: int):
        return cls(user=user, session=Session.objects.get(id=session_id))

    def _get_tickets_for_session(self, amount: int):
        topics = TicketTopic.objects.all().values_list("id", flat=True)[:amount]
        passed_tickets = Ticket.objects.filter(sessions__user=self.user).distinct()
        tickets = list(
            Ticket.objects.exclude(id__in=passed_tickets.values_list("id", flat=True)).filter(
                topic_id__in=topics
            )
        )
        if len(tickets) == 0:
            raise NoTicketsAvailableException()
        random.shuffle(tickets)
        return tickets[:amount]

    def _create_exam(self) -> Session:
        tickets = self._get_tickets_for_session(30)
        self.session = Session.objects.create(
            user=self.user,
            session_type=SessionType.EXAM,
        )
        self.session.tickets.add(*tickets)
        return self.session

    def _create_test(self) -> Session:
        tickets = self._get_tickets_for_session(99)
        self.session = Session.objects.create(
            user=self.user,
            session_type=SessionType.TEST,
        )
        self.session.tickets.add(*tickets)
        return self.session

    def start_session(self, session_type: SessionType) -> Session:
        mapping = {
            SessionType.EXAM: self._create_exam,
            SessionType.TEST: self._create_test,
        }
        method = mapping.get(session_type)
        return method()

    @staticmethod
    def is_exam_finished(
        valid_solved: QuerySet[Ticket],
        invalid_solved: QuerySet[Ticket],
        total: QuerySet[Ticket],
    ) -> bool:
        return len(valid_solved) + len(invalid_solved) == len(total)

    def get_ticket(self, session: Session | None = None) -> tuple[bool, Ticket | None]:
        if not session:
            session = self.session
        valid_solved = session.valid_solved_tickets.all()
        invalid_solved = session.invalid_solved_tickets.all()
        total_ticket = session.tickets.all()
        if self.is_exam_finished(valid_solved, invalid_solved, total_ticket):
            return True, None
        target_ticket = (
            session.tickets.exclude(id__in=valid_solved).exclude(id__in=invalid_solved).first()
        )
        return False, target_ticket

    def add_answer(self, session_id: int, answer_id: int) -> bool:
        self.session = Session.objects.get(id=session_id)
        answer = Answer.objects.get(id=answer_id)
        if answer.is_valid:
            self.session.valid_solved_tickets.add(answer.ticket)
        else:
            self.session.invalid_solved_tickets.add(answer.ticket)
        self.session.save()
        return answer.is_valid

    def get_current_ticket_count(self) -> int:
        valid_solved = self.session.valid_solved_tickets.all()
        invalid_solved = self.session.invalid_solved_tickets.all()
        count = len(valid_solved) + len(invalid_solved) + 1
        return count

    def finish_session(self) -> None:
        self.session.finished_at = timezone.now()
        self.session.save()

    def clear_history(self) -> None:
        sessions = Session.objects.filter(user=self.user)
        for session in sessions:
            session.tickets.clear()

    @property
    def last_session(self) -> Session:
        return Session.objects.filter(user=self.user).order_by("-id").first()

    def decline_last_session(self) -> None:
        self.last_session.set_as_declined()

    def get_last_bot_message_id(self, session_id: int) -> int:
        history: TicketHistory = (
            TicketHistory.objects.filter(
                user=self.user,
                session_id=session_id,
            )
            .order_by("-id")
            .first()
        )
        return history.bot_message_id
