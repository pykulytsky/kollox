from rest_framework import serializers

from todo.models import ToDoItem, SimpleToDoList, Project, Reminder
from authentication.models import User
from authentication.api.serializers import UserSerializer, UserDetailSerializer


class TodoRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        print(type(value))
        if isinstance(value, Project):
            return ProjectListSerializer(value, many=False)
        if isinstance(value, SimpleToDoList):
            return SimpleToDoListListSerializer(value, many=False)
        raise Exception("Unexpected type of list")

class BaseToDoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True, many=False)
    favorite = serializers.BooleanField(default=False)
    status = serializers.CharField(default="Not specified")

    percentage = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)

class BaseToDoListDetailSerializer(serializers.ModelSerializer):
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
    # todo_list = BaseToDoListSerializer(many=False, read_only=True)

    class Meta:
        model = ToDoItem
        fields = '__all__'


class SimpleToDoListListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = SimpleToDoList
        fields = ['id', 'name', 'owner']


class ProjectListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'percentage_completed', 'owner']

    # def create(self, validated_data):
    #     project = Project.objects.create(owner=self.context['request'].user, **validated_data)
    #     return  project


class SimpleToDoListDetailSerializer(serializers.ModelSerializer):
    tasks = ToDoItemDetailSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = SimpleToDoList
        fields = ('id', 'name', 'owner', 'tasks')


class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = ToDoItemDetailSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
