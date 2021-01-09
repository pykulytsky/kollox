import pytest


pytestmark = [pytest.mark.django_db]


def test_project(superuser, project):
    assert project.owner == superuser
    assert project.name == 'Test Project'


def test_simple_todo_list(superuser, simple_list):
    assert simple_list.owner == superuser
    assert simple_list.name == 'Test List'


def test_no_one_user_for_owner_and_shared_owner(superuser, project):
    # TODO move to shared_owners_test.py
    project.shared_owners.add(superuser)
    project.save()

    assert project.owner == project.shared_owners.all().first()
