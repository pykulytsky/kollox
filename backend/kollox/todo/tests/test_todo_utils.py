import pytest

pytestmark = [pytest.mark.django_db]


def test_field_is_changed(project):
    project.name = 'changed name'
    project.save()

    assert project.has_changed


@pytest.mark.xfail(strict=True)
def test_field_is_not_changed(project):

    assert 'name' in project.changed_fields


def test_changed_fields(project):

    project.name = 'changed name'
    project.save()

    # 'id' always in changed_fields
    assert 'name' in project.changed_fields
    assert len(project.changed_fields) > 1


@pytest.mark.xfail(strict=True)
def test_diff_id_only(project):

    assert project.diff['id'][0] == project.diff['id'][1]


def test_diff(project):
    project.name = "changed!"
    project.save()

    assert project.diff['name'][0] == 'Test Project'
    assert project.diff['name'][1] == 'changed!'


def test_get_field_diff(project):
    project.name = "changed!"
    project.save()

    assert project.get_field_diff('name')[0] == 'Test Project'
    assert project.get_field_diff('name')[1] == 'changed!'
