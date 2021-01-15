import pytest
from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def test_register_with_already_used_credentials(anon_api, user):
    url = reverse("register")

    response = anon_api.post(url,
                              {
                                  "username": user.username,
                                  "email": user.email,
                                  "password": user.password
                              })

    assert response.status_code == 400


def test_register(anon_api):
    url = reverse("register")

    response = anon_api.post(url,
                              {
                                  "username": "test_register",
                                  "email": "test@gmail.com",
                                  "password": "12345678"
                              })

    assert response.status_code == 201


def test_login(anon_api):
    # TODO fix login test
    url = reverse("login")

    response = anon_api.post(url,
                              {
                                  "username": "test_register",
                                  "email": "test@gmail.com",
                                  "password": "12345678"
                              },
                              format="json"
                              )

    assert response is not None
