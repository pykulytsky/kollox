import pytest

from rest_framework.test import APIClient


@pytest.fixture
def anon_api():
    client = APIClient()

    return client


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="test",
        password="123456",
        email="test@py.com"
    )

