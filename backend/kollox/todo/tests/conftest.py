import pytest

from authentication.models import User
from rest_framework.test import APIClient
from todo.models import Project, SimpleToDoList, ToDoItem


@pytest.fixture
def superuser():
    user = User.objects.create(
        username="test",
        password="test123456",
        email="test@test.com",
        is_superuser=True
    )
    return user


@pytest.fixture
def project(superuser):
    p = Project.objects.create(owner=superuser,
                               name="Test Project",
                               )

    yield p

    p.delete()


@pytest.fixture
def simple_list(superuser):
    l = SimpleToDoList.objects.create(owner=superuser, name="Test List")

    yield l

    l.delete()


@pytest.fixture
def project_queryset():
    return Project.objects.all()


@pytest.fixture
def simple_list_queryset():
    return Project.objects.all()


@pytest.fixture
def todo_by_simple_list(simple_list):
    todo = ToDoItem.objects.create(title="buy some grapes",
                                   description="I just need some vitamin C",
                                   todo_list=simple_list)

    yield todo

    todo.delete()


@pytest.fixture
def api(superuser):
    client = APIClient()
    token = superuser.token
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    return client


@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        username="another user",
        password="123456",
        email="test@py.com"
    )

@pytest.fixture
def another_project(another_user):
    p = Project.objects.create(owner=another_user,
                               name="Another Test Project",
                               )

    yield p

    p.delete()