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
        User.objects.create(username="pragma3", email="pragma3@mail.com", password="12345678")

    def test_register(self):
        # factory = APIRequestFactory()
        client = APIClient()
        url = reverse('register')
        print(url)
        response = client.post(url,
                               {"username": "pragma4",
                                'email': 'pragma4@mail.com',
                                'password': '12345678'}
                               ,format='json')

        user = User.objects.get(username="pragma3")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bool(user.token), bool(response.data['token']))

    def test_login(self):
        # factory = APIRequestFactory()
        client = APIClient()
        url = reverse('login')
        print(url)
        response = client.post(url,
                               {"username": "pragma3",
                                'email': 'pragma3@mail.com',
                                'password': '12345678'}
                                ,format='json')

        user = User.objects.get(username="pragma3")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bool(user.token), bool(response.data.token))
