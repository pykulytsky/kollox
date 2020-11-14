from django.test import TestCase

from pprint import pprint

from todo.models import SimpleToDoList, Project, Reminder, ToDoItem
from authentication.models import User
# Create your tests here.
class SimpleToDoListTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='pragma', email='pragma@gmail.com', password='12345')
        SimpleToDoList.objects.create(name='Test1', owner=user)
        SimpleToDoList.objects.create(name='Test2', owner=user)
        SimpleToDoList.objects.create(name='Test3', owner=user)

    
    def test_filter_simple_todo_list(self):
        user = User.objects.get(username='pragma')
        lists = SimpleToDoList.objects.filter(owner=user)
        pprint(lists)
        self.assertIsNotNone(lists)

    
    def test_status_field_choise(self):
        todo_list = SimpleToDoList.objects.get(name='Test1')
        todo_list.status = 'test'
        todo_list.save()

        self.assertNotEqual(todo_list.status, 'not_started')


class ProjectTestCase(TestCase):
    def setUp(self):
        pass
