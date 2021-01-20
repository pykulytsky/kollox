import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_project_list_api(api, project):
    url = reverse('projects')

    response = api.get(url)
    data = response.data

    assert response.status_code == 200
    assert len(response.data) > 0


def test_simple_todo_list_list_api(api, simple_list):
    url = reverse("simple-todo-lists")

    response = api.get(url)
    data = response.data

    assert response.status_code == 200
    assert len(response.data) > 0


def test_project_detail_api(api, project, superuser):
    url = reverse('project', kwargs={"id": project.id})

    response = api.get(url)
    data = response.data

    assert response.status_code == 200
    assert response.data['owner']['username'] == superuser.username
    assert response.data['name'] == project.name


def test_simple_todo_list_detail_api(api, simple_list, superuser):
    url = reverse('simple-todo-list', kwargs={"id": simple_list.id})

    response = api.get(url)
    data = response.data

    assert response.status_code == 200
    assert response.data['owner']['username'] == superuser.username
    assert response.data['name'] == simple_list.name
