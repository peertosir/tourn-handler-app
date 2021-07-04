from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPITests(TestCase):
    """Test user API (public)"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Creating user with correct body is successful"""
        payload = {
            'email': 'test@test.ru',
            'password': 'password22',
            'name': 'Test Tester'
        }

        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**resp.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', resp.data)

    def test_create_duplicate_user_fails(self):
        """Test to try create a user that already exists"""
        payload = {
            'email': 'test@test.ru',
            'password': 'password22',
            'name': 'Test Tester'
        }
        create_user(**payload)

        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password must be more than 5 chars"""
        payload = {
            'email': 'test@test.ru',
            'password': 'pwd',
            'name': 'Test Tester'
        }

        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects\
            .filter(email=payload['email']).exists()
        self.assertFalse(user_exists)
