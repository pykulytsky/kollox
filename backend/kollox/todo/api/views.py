from todo.api.serializers import *
from todo.models import *

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from authentication.permissions import UserHasJWTToken, EmailVerified, EmailNotVerified
from todo.models import SimpleToDoList, Project, BaseToDoList
from todo.api.serializers import *
from authentication.models import User

from rest_framework import status
from itertools import chain


class AllToDoListAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, user_id):
        _owner = User.objects.get(id=user_id)
        _simple_todo_lists = SimpleToDoList.objects.filter(owner=_owner)
        _projects = Project.objects.filter(owner=_owner)

        combined_queryset = list(chain(_simple_todo_lists, _projects))
        resulted_query = list()

        for entry in combined_queryset:
            item_type = entry.__class__.__name__.lower()
            serializer = BaseToDoListSerializer(entry)

            resulted_query.append({'todo_list_type': item_type, 'data': serializer.data})

        return Response(resulted_query,
                        status=status.HTTP_200_OK)



    
