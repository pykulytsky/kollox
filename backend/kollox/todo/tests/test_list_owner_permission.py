import pytest
from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def test_user_has_no_permission_to_this_list(api, another_project):
    url = reverse('project', kwargs={"id": another_project.id})

    with pytest.raises(PermissionError):
        api.get(url)


def test_user_has_permission_to_this_list(api, project):
    url = reverse('project', kwargs={"id": project.id})

    response = api.get(url)

    assert response.status_code == 200
    assert response.data['name'] == 'Test Project'