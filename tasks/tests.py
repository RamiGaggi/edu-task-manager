from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from tasks.logger import logger

logger.info('Running tests for task app')


class TasksUserViewsTests(TestCase):
    """Test index view."""

    fixtures = ['data.json']

    def setUp(self):
        """Set data for register and login."""
        self.reg_info = {
            'first_name': 'test3',
            'last_name': 'test3',
            'username': 'test3',
            'password1': 'xcCC_123f5',
            'password2': 'xcCC_123f5',
        }
        self.credentials = {
            'username': 'test1',
            'password': 'http://localhost:8000/',
        }

    def test_index(self):
        """Index test."""
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        """List test."""
        response = self.client.get(reverse('tasks:user-list'))
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        """Test user registration."""
        reg_info = self.reg_info
        response = self.client.get(reverse('tasks:user-create'))
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.client.post(reverse('tasks:user-create'), reg_info)
        self.assertEqual(users.get(username='test3').username, 'test3')
        self.assertEqual(len(users), 4)  # 3 + 1

    def test_login(self):
        """Test user login."""
        response = self.client.get(reverse('tasks:user-login'))
        self.assertEqual(response.status_code, 200)

        credentials = self.credentials
        login = self.client.post(reverse('tasks:user-login'), credentials)
        self.assertEqual(login.status_code, 302)

    def test_delete_update(self):
        """Test user login."""
        response_upd = self.client.get(reverse('tasks:user-update', kwargs={'pk': 77}))  # noqa: E501
        response_del = self.client.get(reverse('tasks:user-delete', kwargs={'pk': 77}))  # noqa: E501
        logger.debug(response_upd)
        self.assertEqual(response_del.status_code, 302)
        self.assertEqual(response_upd.status_code, 302)

        # Update and delete for test1 with pk=77 after login.
        self.client.post(reverse('tasks:user-login'), self.credentials)
        response_upd = self.client.post(
            reverse('tasks:user-update', kwargs={'pk': 77}),
            {'username': 'KwaKwa'},
        )
        users = get_user_model().objects.all()
        self.assertEqual(users.get(pk=77).username, 'KwaKwa')

        response_del = self.client.post(
            reverse('tasks:user-delete', kwargs={'pk': 77}),
        )
        users = get_user_model().objects.all()
        logger.info(users)
        with self.assertRaises(User.DoesNotExist):
            users.get(pk=77)
