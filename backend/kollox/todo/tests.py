from django.test import TestCase

from pprint import pprint

from todo.models import SimpleToDoList, Project, Reminder, ToDoItem
from authentication.models import User
from django.core.mail import send_mail
from decimal import Decimal
from django.conf import settings


class SimpleToDoListTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='pragma', email='pragma@gmail.com', password='12345')
        sl1 = SimpleToDoList.objects.create(name='Test1', owner=user)
        sl2 = SimpleToDoList.objects.create(name='Test2', owner=user)
        sl3 = SimpleToDoList.objects.create(name='Test3', owner=user)
        ToDoItem.objects.create(title='Test todo', description="test description", todo_list=sl1)
        ToDoItem.objects.create(title='Test todo 2', description="test description 2", todo_list = sl1)
        ToDoItem.objects.create(title='Test todo 3', description="test description 3", todo_list=sl2)

    def test_filter_simple_todo_list(self):
        user = User.objects.get(username='pragma')
        lists = SimpleToDoList.objects.filter(owner=user)
        pprint(lists)
        self.assertIsNotNone(lists)

    # def test_status_field_choise(self):
    #     todo_list = SimpleToDoList.objects.get(name='Test1')
    #     todo_list.status = 'test'
    #     todo_list.save()

    #     self.assertNotEqual(todo_list.status, 'not_started')


class ProjectTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='pragma', email='test@gmail.com')
        prj1 = Project.objects.create(name='test1', owner=user)
        prj2 = Project.objects.create(name='test2', owner=user)
        prj3 = Project.objects.create(name='test3', owner=user)

    def test_completed_parcent(self):
        prj = Project.objects.get(name='test1')

        td1 = ToDoItem.objects.create(title='Test todo', description="test description", todo_list=prj)
        td2 = ToDoItem.objects.create(title='Test todo 2', description="test description 2", todo_list=prj)
        td3 = ToDoItem.objects.create(title='Test todo 3', description="test description 3", todo_list=prj)
        prj.save()
        print(f"{prj.tasks.count()=}")
        print(f'{prj.percentage_completed=}')

        td1.is_completed = True
        td2.is_completed = True
        td3.is_completed = True

        td1.save()
        td2.save()
        td3.save()

        prj.save()
        print(f"{prj.tasks.count()=}")
        print(f'{prj.percentage_completed=}')
        
        self.assertEqual(prj.percentage_completed, Decimal('1.0'))

    def test_percentage_validator(self):
        prj = Project.objects.get(name='test1')
        prj.percentage_completed = Decimal('0.1')
        prj.save()
        print(prj.percentage_completed)
        self.assertIsInstance(prj.percentage_completed, Decimal)


class TasksTestCase(TestCase):
    def test_send_share_message(self):
        to_email = 'pykulytsky@gmail.com'

        mail = send_mail(
            'Verify your account',
            'test test test',
            settings.EMAIL_HOST_USER,
            [to_email, ],
            fail_silently=False
        )

        self.assertEqual(mail, 1)
