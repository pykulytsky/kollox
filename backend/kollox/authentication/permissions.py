from .backend import JWTAuthentication
from rest_framework.permissions import BasePermission
from .models import User, UserManager


class EmailVerified(BasePermission):
    """
    Check if current user has verified email
    """

    def has_permission(self, request, view):
        user = request.user
        return bool(user.email_verified)


class EmailNotVerified(BasePermission):
    """
    Check if current user has verified email
    """

    def has_permission(self, request, view):
        user = request.user
        return not bool(user.email_verified)


class UserHasJWTToken(BasePermission):
    """
    Return True if JWT token is already generated for current user,
    and this token is not expired.
    """

    def has_permission(self, request, view):
        user = request.user

        if user.token:
            return True
        else:
            return False


