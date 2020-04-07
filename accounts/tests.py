from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import userProfile

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={"username":"lynn","password":"PASwwordLit","email":"lynn@gmail.com"}
        response=self.client.post('/auth/users/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)