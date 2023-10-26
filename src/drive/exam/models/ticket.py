from django.db import models
from django.template.defaultfilters import truncatechars

from drive.utils.fields import JSONField
from drive.utils.models import BaseModel

from .ticket_category import TicketCategory
from .ticket_image import TicketImage
from .ticket_topic import TicketTopic


class Ticket(BaseModel):
    external_id = models.PositiveIntegerField(verbose_name="External ID")
    question = JSONField(verbose_name="Question")
    image = models.ForeignKey(
        to=TicketImage,
        on_delete=models.CASCADE,
        verbose_name="Image",
        null=True,
        blank=True,
    )
    description = JSONField(verbose_name="Description", null=True, blank=True)
    categories = models.ManyToManyField(
        to=TicketCategory, related_name="tickets", verbose_name="Category"
    )
    topic = models.ForeignKey(
        to=TicketTopic,
        on_delete=models.CASCADE,
        verbose_name="Topic",
        null=True,
    )

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return truncatechars(f"{self.external_id}. {self.question.get('ru')}", 25)

    def get_as_text(
        self,
        session_record,
        ticket_number: int,
        mark_with_color: bool = False,
        chosen_answer: int | None = None,
    ) -> str:
        from .answer import Answer
        from .session import Session

        session_record: Session
        tickets_in_session = len(session_record.tickets.all())

        language = session_record.user.main_language
        original_ticket_address = f"https://teoria.on.ge/tickets?ticket={self.external_id}"

        def get_answer_color_postfix(answer: Answer) -> str:
            if mark_with_color:
                return " 🟢" if answer.is_valid else " 🔴"
            return ""

        prefix = (
            f"{ticket_number}/{tickets_in_session} "
            f"(ID: <a href='{original_ticket_address}'>{self.external_id}</a>)"
        )
        question = self.question.get(language)
        answers = []
        for i, ans in enumerate(self.answers.all()):
            if ans.id == chosen_answer:
                answer = (
                    f"<b>{i + 1}. {ans.answer.get(language)}</b>{get_answer_color_postfix(ans)}"
                )
            else:
                answer = (
                    f"<code>{i + 1}. {ans.answer.get(language)}"
                    f"</code>{get_answer_color_postfix(ans)}"
                )
            answers.append(answer)
        answers = "\n".join(_ for _ in answers)
        message_text = f"{prefix}\n\n{question}\n\n{answers}"
        return message_text
