from django.db import models
from django.conf import settings
from itertools import islice, chain

from decimal import Decimal

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

from authentication.validators import percent_validation

from django.forms.models import model_to_dict

import django.dispatch

# Create your models here.

calculate_percent_signal = django.dispatch.Signal(providing_args=['todo_list_id'])


class QuerySetChain(object):
    """
    Chains multiple subquerysets (possibly of different models) and behaves as
    one queryset.  Supports minimal methods needed for use with
    django.core.paginator.
    """

    def __init__(self, *subquerysets):
        self.querysets = subquerysets

    def count(self):
        """
        Performs a .count() for all subquerysets and returns the number of
        records as an integer.
        """
        return sum(qs.count() for qs in self.querysets)

    def _clone(self):
        "Returns a clone of this queryset chain"
        return self.__class__(*self.querysets)

    def _all(self):
        "Iterates records in all subquerysets"
        return chain(*self.querysets)

    def __getitem__(self, ndx):
        """
        Retrieves an item or slice from the chained set of results from all
        subquerysets.
        """
        if type(ndx) is slice:
            return list(islice(self._all(), ndx.start, ndx.stop, ndx.step or 1))
        else:
            return islice(self._all(), ndx, ndx + 1).next()


class ModelDiffMixin(object):
    """
    Mixin that detects changes in model fields.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        super(ModelDiffMixin, self).save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[field.name for field in
                                           self._meta.fields])


class BaseToDoList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=512, verbose_name="ToDo-List Name")

    favorite = models.BooleanField(default=False, verbose_name="is Favorite")
    cover = models.ImageField(upload_to="assets/avatars/",
                              default="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg")

    class Meta:
        abstract = True


TODO_LIST_STATUS = [
    ('in_archive', 'In Archive'),
    ('started', 'Started'),
    ('completed', 'Completed'),
    ('not_completed', 'Not Completed'),
    ('not_started', 'Not Started')
]


class SimpleToDoList(BaseToDoList):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_simple_todo_lists",
                              verbose_name="ToDo-List Owner")
    tasks = GenericRelation('ToDoItem',
                            content_type_field='todo_list_type',
                            object_id_field='todo_list_id',
                            related_query_name="simple_todo_list")
    status = models.CharField(choices=TODO_LIST_STATUS, max_length=255, default='not_started', verbose_name="Status")

    def save(self, *args, **kwargs):
        if self.status not in [s[0] for s in TODO_LIST_STATUS]:
            raise ValueError(f"Not Valid status. Can be {TODO_LIST_STATUS} not {self.status}.")
        super(SimpleToDoList, self).save(*args, **kwargs)

    class Meta:
        abstract = False
        verbose_name = 'Simple ToDo List'


PROJECT_STATUS = [
    ('in_archive', 'In Archive'),
    ('started', 'Started'),
    ('completed', 'Completed'),
    ('not_complted', 'Not Completed'),
    ('not_started', 'Not Started')
]


class Project(BaseToDoList):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_projects",
                              verbose_name="ToDo-List Owner")
    tasks = GenericRelation('ToDoItem',
                            content_type_field='todo_list_type',
                            object_id_field='todo_list_id',
                            related_query_name="project")
    percentage_completed = models.DecimalField(verbose_name="Completed Status", default=0,
                                               validators=[percent_validation], max_digits=5, decimal_places=2)
    status = models.CharField(choices=PROJECT_STATUS, verbose_name="Status", max_length=256, default='not_started')

    def calculate_percent(self):
        all_tasks = self.tasks.all()
        # TODO Move percent calculation to frontend
        completed_tasks = []
        for task in all_tasks:
            if task.is_completed == True:
                completed_tasks.append(task)

        try:
            _completed_part = Decimal(str(len(completed_tasks) / self.tasks.count()))

            self.percentage_completed = _completed_part
        except ZeroDivisionError:
            self.percentage_completed = Decimal('0.0')

    def __str__(self):
        return f'<Project: {self.name}>'

    def save(self, *args, **kwargs):
        self.calculate_percent()
        if self.status not in [s[0] for s in PROJECT_STATUS]:
            raise ValueError(f"Not Valid status. Can be {PROJECT_STATUS} not {self.status}.")
        super().save(*args, **kwargs)


TODO_ITEM_REPEAT = [
    ('none', 'None'),
    ('every_day', 'Everyday'),
    ('every_hour', 'Every hour'),
    ('custom', 'Custom')
]


class Reminder(models.Model):
    remind_time = models.DateTimeField(blank=True, verbose_name="Remind Time", null=True)

    is_repited = models.BooleanField(default=False, verbose_name="Repeat?")
    repeat_frequency = models.CharField(blank=True, max_length=256, choices=TODO_ITEM_REPEAT, default='none')

    class Meta:
        verbose_name = 'Reminder'
        ordering = ['remind_time']


class ToDoItem(models.Model):
    title = models.CharField(max_length=512, verbose_name="Task Title")
    description = models.TextField(verbose_name="Desctiption", blank=True)
    todo_list_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    todo_list_id = models.PositiveIntegerField()
    todo_list = GenericForeignKey('todo_list_type', 'todo_list_id')
    subtask = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    attached_file = models.FileField(upload_to=f'files/', blank=True)
    attached_photo = models.ImageField(upload_to='images/', blank=True)

    reminder = models.OneToOneField(Reminder, on_delete=models.PROTECT, related_name="reminder_task", blank=True,
                                    null=True)
    remind_me = models.BooleanField(default=False)

    is_completed = models.BooleanField(default=False, verbose_name="Is Completed")
    started_time = models.DateTimeField(auto_now=True, verbose_name='Started time')
    expired_time = models.DateTimeField(verbose_name="Expired Time", blank=True, null=True)

    is_favorite = models.BooleanField(default=False, verbose_name='Is favorite')
    is_important = models.BooleanField(default=False, verbose_name='Is Important')

    def __init__(self, *args, **kwargs):
        super(ToDoItem, self).__init__(*args, **kwargs)
        if self.reminder:
            self.__past_remind_time = self.reminder.remind_time

    def save(self, *args, **kwargs):
        if isinstance(self.todo_list_type, Project):
            list_id = self.todo_list.id
            self.todo_list.calculate_percent()
            # calculate_percent_signal.send(sender=self, todo_list_id=list_id)
        try:
            self.todo_list.calculate_percent()
        except:
            pass
        self.todo_list.save()
        super(ToDoItem, self).save(*args, **kwargs)
        if self.reminder:
            self.__past_remind_time = self.reminder.remind_time

    def __str__(self):
        return f'<ToDoItem {self.pk}:{self.title}>'

    class Meta:
        ordering = ['-started_time', 'is_completed']
        verbose_name = 'Todo Item'
