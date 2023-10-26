from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from drive.exam import models


def ticket_description(request: HttpRequest, pk: int, lang: str) -> HttpResponse:
    try:
        ticket = models.Ticket.objects.get(id=pk)
    except models.Ticket.DoesNotExist:
        raise Http404()
    context = {
        "ticket_number": ticket.external_id,
        "ticket_description": ticket.description.get(lang),
        "bot_name": settings.BOT_USERNAME,
    }
    return render(request, "description.html", context)
