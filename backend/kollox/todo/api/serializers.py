from rest_framework import serializers

from todo.models import ToDoItem, SimpleToDoList, Project, Reminder
from authentication.models import User
from authentication.api.serializers import UserSerializer, UserDetailSerializer

from PIL import Image
from todo.models import Image as ImageModel
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ]
    )

    class Meta:
        model = ImageModel
        fields = ['pk', 'name', 'image']

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
    cover = serializers.ImageField()
    percentage = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    total_tasks = serializers.IntegerField()
    total_completed_tasks = serializers.IntegerField()

class BaseToDoListDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True, many=False)
    favorite = serializers.BooleanField(default=False)
    status = serializers.CharField(default="Not specified")
    cover = serializers.ImageField()
    percentage = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)

    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    total_tasks = serializers.IntegerField()
    total_completed_tasks = serializers.IntegerField()


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'


class ToDoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoItem
        fields = ('id',
                  'title',
                  'is_completed',
                  'is_favorite',
                  'is_important',
                  'todo_list_id',
                  'todo_list_type',
                  'started_time',
                  'expired_time')


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
        fields = ['id',
                  'name',
                  'owner',
                  'total_tasks',
                  'total_completed_tasks']


class ProjectListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id',
                  'name',
                  'percentage_completed',
                  'owner',
                  'cover',
                  'total_tasks',
                  'total_completed_tasks']

    # def create(self, validated_data):
    #     project = Project.objects.create(owner=self.context['request'].user, **validated_data)
    #     return  project


class SimpleToDoListDetailSerializer(serializers.ModelSerializer):
    tasks = ToDoItemDetailSerializer(many=True)
    owner = UserSerializer(read_only=True)
    cover_pick = serializers.IntegerField(required=False)
    shared_owners = UserSerializer(read_only=True, many=True)

    class Meta:
        model = SimpleToDoList
        fields = ('id',
                  'name',
                  'owner',
                  'shared_owners',
                  'cover_pick',
                  'cover',
                  'tasks',
                  'total_tasks')

    def save(self, **kwargs):
        if 'cover_pick' in self.validated_data.keys():
            img = Image.open(f"d:/repos/kollox/frontend/src/assets/cover{self.validated_data['cover_pick']}.jpg")
            cover = img.filename
        super().save(**kwargs)

    def update(self, instance, validated_data):
        if 'cover_pick' in validated_data.keys():
            img = Image.open(f"d:/repos/kollox/frontend/src/assets/cover{self.validated_data['cover_pick']}.jpg")
            instance.cover = img.filename

        instance.name = validated_data.get('name', instance.name)
        instance.favorite = validated_data.get('favorite', instance.favorite)
        
        if 'shared_owners' in validated_data.keys():
            _shared_owner = User.objects.get(id=self.validated_data.get('shared_owners'))
            instance.shared_owners.add(_shared_owner)

        instance.save()
        return instance




class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = ToDoItemDetailSerializer(many=True)
    owner = UserSerializer(read_only=True)
    cover_pick = serializers.IntegerField(required=False)
    shared_owners = UserSerializer(read_only=False, many=True)

    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'owner',
                  'shared_owners',
                  'percentage_completed',
                  'cover_pick',
                  'favorite',
                  'cover',
                  'tasks',
                  'total_tasks',
                  'created',
                  'updated')

    def save(self, **kwargs):
        if 'cover_pick' in self.validated_data.keys():
            img = Image.open(f"d:/repos/kollox/frontend/src/assets/cover{self.validated_data['cover_pick']}.jpg")
            cover = img.filename
        super().save(**kwargs)

    def update(self, instance, validated_data):
        if 'cover_pick' in validated_data.keys():
            img = Image.open(f"d:/repos/kollox/frontend/src/assets/cover{self.validated_data['cover_pick']}.jpg")
            instance.cover = img.filename

        instance.name = validated_data.get('name', instance.name)
        instance.favorite = validated_data.get('favorite', instance.favorite)

        if 'shared_owners' in validated_data.keys():
            _shared_owner = User.objects.get(id=self.validated_data.get('shared_owners'))
            instance.shared_owners.add(_shared_owner)

        instance.save()
        return instance
