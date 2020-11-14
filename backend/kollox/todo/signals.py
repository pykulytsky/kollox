from django.dispatch import receiver
from django.db.models.signals import post_save

from todo.models import ToDoItem, Project, calculate_percent_signal


@receiver(calculate_percent_signal, sender=ToDoItem)
def calculate_percents_signal(sender, **kwargs):
    _project = Project.objects.get(id=kwargs.get('todo_list_id'))
    _project.calculate_percent()
    _project.save()
