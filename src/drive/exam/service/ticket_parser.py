import io
import os
from io import BytesIO
from typing import Dict, List

import requests
from bs4 import BeautifulSoup, Tag
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from google.cloud import translate_v2 as translate
from loguru import logger
from PIL import Image, ImageOps
from pydantic import BaseModel

from drive.bot.const import Language
from drive.exam import models


class Answer(BaseModel):
    text: dict[str, str]
    is_valid: bool


class TicketImage(BaseModel):
    file_bytes: bytes
    file_name: str


class Ticket(BaseModel):
    external_id: int
    topic_id: int
    categories_ids: List[int]
    image: TicketImage | None
    question: Dict[str, str]
    description: Dict[str, str]
    answers: List[Answer] | None


class TicketParser:
    @staticmethod
    def _get_html(url: str) -> str:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(
                f"Error while sending request, info: {url=}, status_code={response.status_code}"
            )
        return response.text

    def _extract_answers(self, ticket_container: Tag) -> List[Dict[str, str | bool]]:
        answer_tags = ticket_container.select("p.t-answer:not(.ans-empty)")
        answers = []
        for answer in answer_tags:
            answer_text = answer.find("span", class_="text-wrap").text
            answers.append(
                {
                    "text": self._translate_text(answer_text),
                    "is_valid": "data-is-correct-list" in answer.attrs,
                }
            )
        return answers

    @staticmethod
    def _download_image(url: str) -> Image:
        response = requests.get(url)
        img_raw = Image.open(BytesIO(response.content))
        return img_raw

    @staticmethod
    def _convert_image_to_1bit(image: Image) -> Image:
        img_bw = ImageOps.grayscale(image)
        img_1bit = img_bw.point(lambda x: 0 if x < 128 else 255, "1")
        return img_1bit

    @staticmethod
    def _crop_image(image_1bit: Image, original_image: Image) -> bytes:
        width, height = image_1bit.size
        break_point = height
        for y in range(height):
            if all(image_1bit.getpixel((x, y)) == 0 for x in range(15, width - 15)):
                break_point = y
                break
        cropped_img = original_image.crop((0, 0, width, break_point))
        img_io = BytesIO()
        cropped_img.save(img_io, format="JPEG")
        img_content = img_io.getvalue()
        return img_content

    def _extract_image(self, ticket_container: Tag) -> TicketImage | None:
        image = ticket_container.find("figure", class_="t-image")
        if image:
            url = image.find("img").get("src")
            file_name = url.split("/")[-1]
            img = self._download_image(url)
            img_1bit = self._convert_image_to_1bit(img)
            cropped_image = self._crop_image(img_1bit, img)
            return TicketImage(file_name=file_name, file_bytes=cropped_image)

    @staticmethod
    def _extract_topic_id(page: BeautifulSoup) -> int:
        topic_url = page.find("a", class_="light", attrs={"data-category-link-pattern": True}).get(
            "href"
        )
        topic_id = int(topic_url.split("/")[-1])
        return topic_id

    @staticmethod
    def _extract_categories_ids(page: BeautifulSoup) -> List[int]:
        categories = page.find("span", class_="single-ticket-cats-list").find_all("a")
        categories_ids = []
        for category in categories:
            category_id = int(category.get("href").split("/")[-2])
            categories_ids.append(category_id)
        return categories_ids

    @staticmethod
    def _translate_text(text: str) -> dict:
        source_language = Language.GEORGIAN
        target_languages = [
            Language.AZERBAIJANI,
            Language.ENGLISH,
            Language.ARMENIAN,
            Language.RUSSIAN,
            Language.TURKISH,
            Language.UKRAINIAN,
        ]
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(settings.ROOT_DIR, "creds.json")
        client = translate.Client()
        translations = {Language.GEORGIAN: text}
        for lang in target_languages:
            if text == "":
                translations[lang] = ""
                continue
            response = client.translate(text, source_language=source_language, target_language=lang)
            translations[lang] = response["translatedText"]
        return translations

    def _extract_question(self, ticket_container: Tag) -> Dict[str, str]:
        question = (
            ticket_container.find("p", class_="t-question-inner")
            .find("span", class_="text-wrap")
            .text
        )
        return self._translate_text(question)

    def _extract_description(self, page: BeautifulSoup) -> Dict[str, str]:
        description = page.find("div", class_="desc-box").find("p").text
        return self._translate_text(description)

    def _get_as_ticket_instance(self, html: str, ticket_id: int):
        soup = BeautifulSoup(html, "html.parser")
        ticket_container = soup.find("article", class_="ticket-container")
        if not ticket_container:
            return
        topic_id = self._extract_topic_id(soup)
        categories_ids = self._extract_categories_ids(soup)
        image = self._extract_image(ticket_container)
        question = self._extract_question(ticket_container)
        description = self._extract_description(soup)
        answers = self._extract_answers(ticket_container)
        ticket = Ticket(
            external_id=ticket_id,
            topic_id=topic_id,
            categories_ids=categories_ids,
            image=image,
            question=question,
            description=description,
            answers=[Answer(text=ans.get("text"), is_valid=ans.get("is_valid")) for ans in answers],
        )
        return ticket

    def _parse_ticket(self, ticket_id: int) -> Ticket:
        url = f"https://teoria.on.ge/tickets?ticket={ticket_id}"
        html = self._get_html(url)
        return self._get_as_ticket_instance(html, ticket_id)

    def find_new_tickets(
        self, last_known_ticket_id: int | None = None, look_for: int = 10
    ) -> List[Ticket]:
        if not last_known_ticket_id:
            last_known_ticket_id: int = (
                models.Ticket.objects.all().order_by("-external_id").first().external_id
            )
        external_ticket_id = last_known_ticket_id
        tickets = []
        for _ in range(look_for):
            external_ticket_id += 1
            ticket = self._parse_ticket(external_ticket_id)
            if ticket:
                tickets.append(ticket)
                look_for += 1
        return tickets

    @staticmethod
    def _save_image(image: Image) -> models.TicketImage:
        image_pil = Image.open(io.BytesIO(image.file_bytes))
        output = io.BytesIO()
        image_pil.save(output, format="JPEG")
        output.seek(0)
        file = InMemoryUploadedFile(
            output, image.file_name, image.file_name, "image/jpeg", len(output.getvalue()), None
        )
        record = models.TicketImage.objects.create(image=file)
        return record

    def save_tickets(self, tickets: List[Ticket]):
        for ticket in tickets:
            if ticket.image:
                image = self._save_image(ticket.image)
            else:
                image = None
            new_ticket = models.Ticket.objects.create(
                external_id=ticket.external_id,
                question=ticket.question,
                image=image,
                description=ticket.description,
                topic_id=ticket.topic_id,
            )
            categories = models.TicketCategory.objects.filter(category_id__in=ticket.categories_ids)
            new_ticket.categories.add(*categories)
            for answer in ticket.answers:
                models.Answer.objects.create(
                    ticket=new_ticket, answer=answer.text, is_valid=answer.is_valid
                )
            logger.info(f"New ticket with id #{ticket.external_id} has been added")
