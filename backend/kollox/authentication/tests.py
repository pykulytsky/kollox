from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APIClient
from django.urls import reverse

from .models import User
from .api.views import *
from .api.serializers import *
# Create your tests here.

class AuthTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="test", email="test@mail.com", password="12345678")

    def test_login(self):
        # factory = APIRequestFactory()
        client = APIClient()
        response = client.post('http://localhost:8000/login',
                               {"username": "pragma3",
                                'email': 'pragma3@mail.com',
                                'password': '12345678'}
                               )

        user = User.objects.get(username="test")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.token, response.data.token)