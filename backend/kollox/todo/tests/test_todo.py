import pytest
from todo.models import ToDoItem
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def subtask(superuser, simple_list):
    task = ToDoItem.objects.create(title="go to door",
                                      todo_list=simple_list)

    return task


def test_base_todo(todo_by_simple_list, superuser, simple_list):

    assert todo_by_simple_list.todo_list == simple_list
    assert todo_by_simple_list.todo_list.owner == superuser
    assert todo_by_simple_list.title == 'buy some grapes'


def test_subtask(todo_by_simple_list, superuser, simple_list, subtask):
    todo_by_simple_list.subtask = subtask
    todo_by_simple_list.save()

    assert todo_by_simple_list.subtask.title == 'go to door'


def test_favorites_tasks(todo_by_simple_list, api):
    todo_by_simple_list.is_favorite = True
    todo_by_simple_list.save()

    url = reverse('favorite_todos')
    response = api.get(url)

    assert response.status_code == 200
    assert False, response.data

