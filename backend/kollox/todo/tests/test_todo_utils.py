import pytest


pytestmark = [pytest.mark.django_db]


def test_field_is_changed(project)