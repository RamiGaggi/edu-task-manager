from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from tasks.logger import logger
from tasks.models import Status

logger.info('Running tests for task app')


class TasksUserViewsTests(TestCase):
    """Test views for user."""

    fixtures = ['user_data.json']

    def setUp(self):
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
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get(reverse('tasks:user-list'))
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        reg_info = self.reg_info
        response = self.client.get(reverse('tasks:user-create'))
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.client.post(reverse('tasks:user-create'), reg_info)
        self.assertEqual(users.get(username='test3').username, 'test3')
        self.assertEqual(users.count(), 4)  # 3 + 1

    def test_login(self):
        response = self.client.get(reverse('tasks:user-login'))
        self.assertEqual(response.status_code, 200)

        credentials = self.credentials
        login = self.client.post(reverse('tasks:user-login'), credentials)
        self.assertEqual(login.status_code, 302)

    def test_delete_update(self):
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
        with self.assertRaises(User.DoesNotExist):
            users.get(pk=77)


class TasksStatusViewsTests(TestCase):
    """Test status views."""

    fixtures = ['status_data.json']

    def setUp(self):
        self.credentials = {
            'username': 'test1',
            'password': 'http://localhost:8000/',
        }
        self.login = self.client.post(
            reverse('tasks:user-login'),
            self.credentials,
        )
        self.status = Status

    def test_list(self):
        url = reverse('tasks:status-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        url = reverse('tasks:status-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.post(url, {'name': 'In Review'})
        self.assertEqual(Status.objects.all().count(), 5)  # 4 + 1
        self.assertEqual(Status.objects.get(name='In Review').name, 'In Review')  # noqa: E501

    def test_update(self):
        url = reverse('tasks:status-update', kwargs={'pk': 20})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.post(url, {'name': 'Big DEAL'})
        self.assertEqual(Status.objects.get(pk=20).name, 'Big DEAL')

    def test_delete(self):
        url = reverse('tasks:status-delete', kwargs={'pk': 20})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.post(url)
        with self.assertRaises(Status.DoesNotExist):
            self.assertEqual(Status.objects.get(pk=20))
