from django.http import response
import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_list_patch_url(project):
    url = reverse("project", kwargs={"id": project.id})

    assert url == f'/api/todo/project/{project.id}/'


def test_project_patch_name(project, api):
    url = reverse('project', kwargs={'id': project.id})

    response = api.patch(url, {'name': 'test'})

    assert response.status_code == 200
    assert response.data['name'] == 'test'


def test_simple_list_patch_name(simple_list, api):
    url = reverse('simple-todo-list', kwargs={'id': simple_list.id})

    response = api.patch(url, {'name': 'test'})

    assert response.status_code == 200
    assert response.data['name'] == 'test'


def test_project_patch_cover(project, api):
    url = reverse("project", kwargs={"id": project.id})

    response = api.patch(url, {
        'cover_pick': 1
    })

    assert response.status_code == 200
    assert 'cover1.jpg' in response.data['cover']


def test_simple_list_patch_cover(simple_list, api):
    url = reverse("simple-todo-list", kwargs={"id": simple_list.id})

    response = api.patch(url, {
        'cover_pick': 1
    })

    assert response.status_code == 200
    assert 'cover1.jpg' in response.data['cover']


def test_project_shared_owners_patch(project, api, another_user):
    url = reverse("project", kwargs={"id": project.id})

    response = api.patch(url, {
        'shared_owners': another_user.id
    })

    assert response.status_code == 200


def test_simple_list_shared_owners_patch(simple_list, api, another_user):
    url = reverse("simple-todo-list", kwargs={"id": simple_list.id})

    response = api.patch(url, {
        'shared_owners': another_user.id
    })

    assert response.status_code == 200

