from django.db import models
from django.conf import settings
# Create your models here.
class BaseToDoList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SimpleToDoList(BaseToDoList):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_simple_todo_lists", verbose_name="ToDo-List Owner")
    pass


class Project(BaseToDoList):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_projects", verbose_name="ToDo-List Owner")
    pass


class BaseToDoItem(models.Model):
    
    class Meta:
        abstract = True