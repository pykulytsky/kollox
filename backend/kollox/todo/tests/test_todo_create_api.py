from todo.tests.conftest import simple_list
from django.http import response
import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_todo_create_url():
    url = reverse('todo_items_list')

    assert url == '/api/todo/todos/'


def test_create_todo_item_on_project(api, project):
    url = reverse('todo_items_list')

    response = api.post(url, {
        'title': 'test todo',
        'todo_list_id': project.id,
        'todo_list_type': 10
    })

    assert response.status_code == 201
    assert response.data['title'] == 'test todo'


def test_create_todo_item_on_simple_list(api, simple_list):
    url = reverse('todo_items_list')

    response = api.post(url, {
        'title': 'test todo',
        'todo_list_id': simple_list.id,
        'todo_list_type': 9
    })

    assert response.status_code == 201
    assert response.data['title'] == 'test todo'


def test_create_todo_list_changed(api, project):
    url = reverse('todo_items_list')

    response = api.post(url, {
        'title': 'test todo',
        'todo_list_id': project.id,
        'todo_list_type': 10
    })

    project_url = reverse('project', kwargs={'id': project.id})
    project_response = api.get(project_url)

    
    assert response.status_code == 201
    assert len(project_response.data['tasks']) == 0
