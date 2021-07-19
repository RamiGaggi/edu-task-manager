from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from tasks.logger import logger
from tasks.models import Status, Task

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
        url = reverse('tasks:index')
        response = self.client.get(url)  # noqa: WPS204 Overused expression
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        url = reverse('tasks:user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        reg_info = self.reg_info
        url = reverse('tasks:user-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.client.post(url, reg_info)
        self.assertEqual(users.get(username='test3').username, 'test3')
        self.assertEqual(users.count(), 4)  # 3 + 1

    def test_login(self):
        url = reverse('tasks:user-login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        credentials = self.credentials
        login = self.client.post(url, credentials)
        self.assertEqual(login.status_code, 302)

    def test_delete_update(self):
        url_update = reverse('tasks:user-update', kwargs={'pk': 77})
        url_delete = reverse('tasks:user-delete', kwargs={'pk': 77})
        response_upd = self.client.get(url_update)
        response_del = self.client.get(url_delete)
        self.assertEqual(response_del.status_code, 302)
        self.assertEqual(response_upd.status_code, 302)

        # Update and delete for test1 with pk=77 after login.
        self.client.post(reverse('tasks:user-login'), self.credentials)
        response_upd = self.client.post(url_update, {'username': 'KwaKwa'})
        users = get_user_model().objects.all()
        self.assertEqual(users.get(pk=77).username, 'KwaKwa')

        response_del = self.client.post(url_delete, kwargs={'pk': 77})
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


class TasksViewsTests(TestCase):
    """Test status views."""

    fixtures = ['task_data.json']

    def setUp(self):
        self.credentials = {
            'username': 'test1',
            'password': 'http://localhost:8000/',
        }
        self.login = self.client.post(
            reverse('tasks:user-login'),
            self.credentials,
        )

        self.task = {
            'name': 'test task',
            'description': 'smth',
            'status': 21,
            'executor': 79,
        }

    def test_single(self):
        url = reverse('tasks:task', kwargs={'pk': 10})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        url = reverse('tasks:task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        url = reverse('tasks:task-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.post(url, self.task)
        self.assertEqual(Task.objects.all().count(), 7)  # 6 + 1
        self.assertEqual(Task.objects.get(name='test task').id, 12)  # noqa: E501

    def test_update(self):
        url = reverse('tasks:task-update', kwargs={'pk': 10})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.post(url, self.task)
        self.assertEqual(Task.objects.get(pk=10).name, 'test task')

    def test_delete(self):
        url = reverse('tasks:task-delete', kwargs={'pk': 10})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.post(url)
        with self.assertRaises(Task.DoesNotExist):
            self.assertEqual(Task.objects.get(pk=10))
