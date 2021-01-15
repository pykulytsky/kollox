import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_create_url():
    url = reverse('projects')

    assert url == '/api/todo/projects/'


def test_project_create_api(api, superuser):
    url = reverse('projects')

    response = api.post(url, {
        'name': 'new project',
    })

    assert response.status_code == 201
    assert response.data['name'] == 'new project'
    assert response.data['owner']['pk'] == superuser.id
    assert response.data['percentage_completed'] == '0.00'


def test_simple_list_create_api(api, superuser):
    url = reverse('simple-todo-lists')

    response = api.post(url, {
        'name': 'new simple list',
    })

    assert response.status_code == 201
    assert response.data['name'] == 'new simple list'
    assert response.data['owner']['pk'] == superuser.id
