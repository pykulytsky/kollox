from ..api.serializers import *
from ..models import *

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from authentication.permissions import UserHasJWTToken, EmailVerified, EmailNotVerified
from ..models import SimpleToDoList, Project, BaseToDoList
from ..api.serializers import *
from authentication.models import User

from rest_framework import status
from itertools import chain

from rest_framework import generics


class AllToDoListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        _owner = request.user
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


class SimpleToDoListListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SimpleToDoListListSerializer

    def get_queryset(self, request):
        queryset = SimpleToDoList.objects.filter(owner=request.user)
        return queryset

    def list(self, request):
        queryset = Project.objects.filter(owner=request.user)
        serializer = self.serializer_class(self.get_queryset(request), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    # def get(self, request):
    #     _owner = request.user
    #     _simple_todo_lists = SimpleToDoList.objects.filter(owner=_owner)
    #
    #     serializer = self.serializer_class(_simple_todo_lists, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectListSerializer

    def get_queryset(self, request):
        queryset = Project.objects.filter(owner=request.user)
        return queryset

    def list(self, request):
        queryset = Project.objects.filter(owner=request.user)
        serializer = self.serializer_class(self.get_queryset(request), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_serializer_context(self):
    #     return {"request": self.request}

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # def get(self, request):
    #     _owner = request.user
    #     _simple_todo_lists = Project.objects.filter(owner=_owner)
    #
    #     serializer = self.serializer_class(_simple_todo_lists, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     print(request.data)
    #     print(f'{request.user=}')
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SimpleToDoListDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SimpleToDoListDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = SimpleToDoList.objects.all()


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = Project.objects.all()
    # permission_classes = (IsAuthenticated,)
    # serializer_class = ProjectDetailSerializer
    #
    # def get(self, request, id):
    #     todo_list = Project.objects.get(id=id)
    #     serializer = self.serializer_class(todo_list)
    #
    #     return Response(serializer.data,
    #                     status=status.HTTP_200_OK)


class ToDoItemListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ToDoItemSerializer

    def get_queryset(self, request):
        queryset = ToDoItem.objects.filter(
            todo_list_id=request.data['list_id'],
            todo_list_type=request.data['list_type'])
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(request), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ToDoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoItemDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = ToDoItem.objects.all()
