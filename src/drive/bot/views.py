from urllib.parse import urljoin

from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from telebot import types

from drive.bot import communication  # noqa
from drive.bot.conf import bot


def set_webhook(request: HttpRequest) -> HttpResponseRedirect:
    if request.user.is_superuser:
        bot.delete_webhook()
        webhook_url = urljoin(settings.PROJECT_URL, "/bot/new-update/")
        bot.set_webhook(webhook_url, secret_token=settings.TELEGRAM_SECRET_KEY)
        return HttpResponseRedirect("/admin/")
    else:
        raise Http404()


@csrf_exempt
def new_update(request: HttpRequest) -> HttpResponse:
    json_string = request.body.decode("UTF-8")
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return HttpResponse(status=200)
