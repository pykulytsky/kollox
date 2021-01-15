import jwt

from django.conf import settings
from rest_framework import authentication, exceptions
from authentication.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    _AUTHENTICATION_HEADER_PREFIX = 'Bearer'

    def authenticate(self, request) -> tuple:
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self._AUTHENTICATION_HEADER_PREFIX.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token) -> tuple:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            message = 'Не можу автентифікувати, неправельний токен'
            raise exceptions.AuthenticationFailed(message)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)
        if not user.is_active:
            message = 'Неактивний користувач.'
            raise exceptions.AuthenticationFailed(message)

        return (user, token)
