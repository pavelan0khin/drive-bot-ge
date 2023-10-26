import gettext as gt
import os

from django.conf import settings


def translations():
    path = os.path.join(settings.BASE_DIR, "bot/i18n/locales")
    if not os.path.exists(path):
        raise RuntimeError(f"Translations directory by path: {path!r} was not found")
    result = {}
    for name in os.listdir(path):
        translations_path = os.path.join(path, name, "LC_MESSAGES")
        if not os.path.isdir(translations_path):
            continue
        po_file = os.path.join(translations_path, "messages" + ".po")
        mo_file = po_file[:-2] + "mo"
        if os.path.isfile(po_file) and not os.path.isfile(mo_file):
            raise FileNotFoundError(f"Translations for: {name!r} were not compiled!")
        with open(mo_file, "rb") as file:
            result[name] = gt.GNUTranslations(file)
    return result


def gettext(text: str, language: str):
    translator = translations()[language]
    return translator.gettext(text)
