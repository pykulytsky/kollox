from ..api.serializers import *
from ..models import *
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from authentication.permissions import UserHasJWTToken, EmailVerified, EmailNotVerified
from ..permissions import ListOwnerPermission
from ..models import SimpleToDoList, Project, BaseToDoList
from ..api.serializers import *
from authentication.models import User
from django.db.models import Q

from rest_framework import status
from itertools import chain

from rest_framework import generics

from todo.tasks import send_share_message


class AllToDoListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        _owner = request.user
        _simple_todo_lists = SimpleToDoList.objects.filter(Q(owner=_owner) | Q(shared_owners=_owner))
        _projects = Project.objects.filter(Q(owner=_owner) | Q(shared_owners=_owner))

        combined_queryset = list(chain(_simple_todo_lists, _projects))
        resulted_query = list()

        for entry in combined_queryset:
            item_type = entry.__class__.__name__.lower()
            serializer = BaseToDoListSerializer(entry,
                                                context={"request": request})

            resulted_query.append({'todo_list_type': item_type,
                                   'data': serializer.data})

        return Response(resulted_query,
                        status=status.HTTP_200_OK)


class SimpleToDoListListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SimpleToDoListListSerializer

    def get_queryset(self, request):
        _owner = request.user
        queryset = SimpleToDoList.objects.filter(Q(owner=_owner) | Q(shared_owners=_owner))
        return queryset

    def list(self, request):
        _owner = request.user
        queryset = SimpleToDoList.objects.filter(Q(owner=_owner) | Q(shared_owners=_owner))
        serializer = self.serializer_class(self.get_queryset(request),
                                           many=True,
                                           context={"request": request})

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
        _owner = request.user
        queryset = Project.objects.filter(Q(owner=_owner) | Q(shared_owners=_owner))
        return queryset

    def list(self, request):
        _owner = request.user
        serializer = self.serializer_class(self.get_queryset(request),
                                           many=True,
                                           context={"request": request})

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
    permission_classes = (IsAuthenticated, ListOwnerPermission)
    serializer_class = SimpleToDoListDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = SimpleToDoList.objects.all()
    # TODO add protection for current user


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ListOwnerPermission)
    serializer_class = ProjectDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = Project.objects.all()

    def patch(self, request, id, *args, **kwargs):
        if 'shared_owners' in request.data.keys():
            _project = Project.objects.get(id=id)
            try:
                shared_owner = User.objects.get(id=request.data['shared_owners'])
                _project.shared_owners.add(shared_owner)
                _project.save()

                send_share_message.apply_async(eta=datetime.datetime.now() + datetime.timedelta(minutes=1),
                                               kwargs={'to_email': shared_owner.email})

                serializer = self.serializer_class(_project)
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            except:
                return Response({
                    'detail': 'User does not exists'
                },
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return super().patch(request, *args, **kwargs)

    # def patch(self, request, id, *args, **kwargs):
    #     _project = Project.objects.get(id=id)
    #     if 'shared_owners' in request.data.keys():
    #         try:
    #             shared_owner = User.objects.get(id=request.data['shared_owners'])
    #             _project.shared_owners.add(shared_owner)
    #             _project.save()
    #             serializer = self.serializer_class(_project)
    #             return Response(serializer.data,
    #                             status=status.HTTP_200_OK)
    #         except Project.DoesNotExists:
    #             return Response({
    #                 'detail': 'User does not exists'
    #             },
    #                             status=status.HTTP_404_NOT_FOUND)
    #     else:
    #             # TODO Fix serializer
    #         serializer = self.serializer_class(_project, data=request.data, many=False)
    #         # serializer.update(_project, serializer.validated_data)
    #         # return Response(serializer.data,
    #         #                 status=status.HTTP_200_OK)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data,
    #                             status=status.HTTP_200_OK)
    #         else:
    #             return Response({
    #                 'detail': 'Wrong data in data field'
    #             })

    # def patch(self, request, id):
    #     image_src = request.data['cover']
    #     cover = open('d:/repos/kollox/frontend/src/assets/' + image_src)
    #     project = Project.objects.get(id=id)
    #     project.cover = cover
    #     project.save()
    #     serializer = self.serializer_class(project)
    #     if serializer.is_valid():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
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
        _user = request.user
        if 'list_id' in request.data.keys() and 'list_type' in request.data.keys():
            if request.data['list_type'] == 10:
                queryset = ToDoItem.objects.filter(
                    Q(project__owner=_user) | Q(project__shared_owners=_user),
                    todo_list_id=request.data['list_id'],
                    todo_list_type=request.data['list_type'],
                    ).order_by('id')
            else:
                queryset = ToDoItem.objects.filter(
                    Q(project__owner=_user) | Q(project__shared_owners=_user),
                    todo_list_id=request.data['list_id'],
                    todo_list_type=request.data['list_type'],
                ).order_by('id')
        else:
            try:
                queryset = ToDoItem.objects.filter(
                    Q(project__owner=_user) | Q(project__shared_owners=_user)
                ).order_by('id')
            except:
                queryset = ToDoItem.objects.filter(
                    Q(project__owner=_user) | Q(project__shared_owners=_user)
                ).order_by('id')
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(request),
                                           many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FavoriteToDoItemListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ToDoItemSerializer

    def get_queryset(self, request):

        _user = request.user
        if 'list_id' in request.data.keys() and 'list_type' in request.data.keys():
            if request.data['list_type'] == 10:
                queryset = ToDoItem.objects.filter(
                    todo_list_id=request.data['list_id'],
                    todo_list_type=request.data['list_type'],
                    project__owner=_user,
                    is_favorite=True
                )
            else:
                queryset = ToDoItem.objects.filter(
                    todo_list_id=request.data['list_id'],
                    todo_list_type=request.data['list_type'],
                    simple_todo_list__owner=_user,
                    is_favorite=True
                )
        else:
            try:
                queryset = ToDoItem.objects.filter(
                    is_favorite=True,
                    project__owner=_user
                )
            except:
                queryset = ToDoItem.objects.filter(
                    is_favorite=True,
                    simple_todo_list__owner=_user
                )
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(request),
                                           many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ToDoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoItemDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = ToDoItem.objects.all()
