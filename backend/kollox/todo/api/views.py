from todo.api.serializers import *
from todo.models import *

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from authentication.permissions import UserHasJWTToken, EmailVerified, EmailNotVerified

from rest_framework import status


class AllToDoListAPI(APIView):
    
