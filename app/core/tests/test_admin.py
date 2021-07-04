from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='password123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@user.com',
            password='PassWord321',
            name='Test user full name'
        )

    def test_users_are_listed_in_admin_panel(self):
        """Test that users are listed in users section"""
        url = reverse('admin:core_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.email)
        self.assertContains(resp, self.user.name)

    def test_user_edit_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
