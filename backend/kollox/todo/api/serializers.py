from rest_framework import serializers

from todo.models import ToDoItem, SimpleToDoList, Project, Reminder
from authentication.models import User
from authentication.api.serializers import UserSerializer, UserDetailSerializer
class BaseToDoListSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True, many=False)
    favorite = serializers.BooleanField(default=False)
    status = serializers.CharField(default="Not specified")

    percentage = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)

class BaseToDoListDetailSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True, many=False)
    favorite = serializers.BooleanField(default=False)
    status = serializers.CharField(default="Not specified")

    percentage = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)

    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('title', 'is_completed', 'is_favorite', 'is_important')


class ToDoItemDetailSerializer(serializers.ModelSerializer):
    reminder = ReminderSerializer(many=False)
    todo_list = BaseToDoListSerializer(many=False, read_only=True)
    class Meta:
        model = ToDoItem
        fields = '__all__'


class SimpleToDoListListSerializer(serializers.ModelSerializer):
    pass
