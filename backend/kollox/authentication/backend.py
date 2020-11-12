from django.conf import settings
from rest_framework import authentication, exceptions
from django.contrib.auth import authenticate
from authentication.models import User, UserManager

import jwt
from jwt.exceptions import *

from django.contrib.auth.backends import BaseBackend

from typing import Union, Any


class JWTAuthenticationBackend(authentication.BaseAuthentication):
    """
    Implements JWT authentication, method authenticate returns None or tuple of user and jwt token.
    Returns None when:
    1. In request Authorization header is no jwt token
    2. In request Authorization header is no authentication prefix 'Bearer'
    In other cases return tuple of user adn jwt token
    """
    _AUTHENTICATION_HEADER_PREFIX = 'Bearer'

    def _authenticate_credentials(self, request, token: jwt) -> tuple:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except (InvalidTokenError, DecodeError, InvalidAlgorithmError,
                InvalidAudienceError, ExpiredSignatureError, ImmatureSignatureError,
                InvalidIssuedAtError, InvalidIssuerError, ExpiredSignature,
                InvalidAudience, InvalidIssuer, MissingRequiredClaimError,
                InvalidSignatureError,
                PyJWTError):
                raise exceptions.AuthenticationFailed(f"<JWTToken {token}> Cant  authenticate")
        try:
            user = User.objects.get(id=payload.get('id'))
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(f"<JWTToken {token}> Cant find user with such authentication credentials.")

        if not user.is_active:
            raise exceptions.AuthenticationFailed(f"<User {user.username}> is not active.")
            
        return (user, token)

    
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
