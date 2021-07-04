from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Testqwert12'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for a new user is normalized"""
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password='Test1234'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='Test1234'
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='Test1234'
            )

    def test_new_super_user_created(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_super_user(
            email="test@test.com",
            password='1123Test'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
