from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from drive.bot.models import APIToken


class CustomTokenAuthentication(TokenAuthentication):
    model = APIToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related("user").get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token."))
        if token.user.is_blocked:
            raise exceptions.AuthenticationFailed(_("User inactive or deleted."))
        return token.user, token
