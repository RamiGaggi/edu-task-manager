import logging
import sys

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from tasks.models import Label, MyUser, Status, Task
from tasks.tests.base import TaskMixinTest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class TasksUserViewsTests(TaskMixinTest, TestCase):
    """Test views for user."""

    list_page = 'tasks:user-list'
    create_page = 'tasks:user-create'
    update_page = 'tasks:user-update'
    update_args = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'username': 'Kwa',
        'password1': 'levox3fgv',
        'password2': 'levox3fgv',
    }
    delete_page = 'tasks:user-delete'
    kwargs = {'pk': 3}
    model = MyUser

    def setUp(self):
        pass  # noqa: WPS420

    def test_index(self):
        url = reverse(self.index_page)
        self.get_check_page(url)

    def test_registration(self):
        reg_info = self.reg_info
        url = reverse(self.create_page)
        self.get_check_page(url)

        users = get_user_model().objects.all()
        self.client.post(url, reg_info)
        self.assertEqual(users.get(username='test3').username, 'test3')
        self.assertEqual(users.count(), 4)  # 3 + 1

    def test_login(self):
        url = reverse('tasks:user-login')
        self.get_check_page(url)
        credentials = self.credentials
        login = self.client.post(url, credentials)
        self.assertEqual(login.status_code, 302)

    def test_update(self):
        self.client.post(reverse('tasks:user-login'), self.credentials)
        instances = super().test_update()
        self.assertEqual(instances.get(pk=self.kwargs['pk']).username, 'Kwa')

    def test_delete(self):
        self.client.post(reverse('tasks:user-login'), self.credentials)
        super().test_delete()


class TasksStatusViewsTests(TaskMixinTest, TestCase):
    """Test status views."""

    list_page = 'tasks:status-list'
    create_page = 'tasks:status-create'
    update_page = 'tasks:status-update'
    update_args = {'name': 'Big DEAL'}
    delete_page = 'tasks:status-delete'
    kwargs = {'pk': 3}
    model = Status

    def test_update(self):
        instances = super().test_update()
        self.assertEqual(instances.get(pk=self.kwargs['pk']).name, 'Big DEAL')


class TaskTaskTests(TaskMixinTest, TestCase):
    """Test status views."""

    list_page = 'tasks:task-list'
    create_page = 'tasks:task-create'
    update_page = 'tasks:task-update'
    update_args = {
        'name': 'test task',
        'description': 'smth',
        'status': 3,
        'executor': 2,
    }
    delete_page = 'tasks:task-delete'
    kwargs = {'pk': 4}
    model = Task

    def test_update(self):
        instances = super().test_update()
        self.assertEqual(instances.get(pk=self.kwargs['pk']).name, 'test task')

    def test_single(self):
        url = reverse('tasks:task', kwargs={'pk': 3})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TasksLabelTests(TaskMixinTest, TestCase):
    """Test status views."""

    list_page = 'tasks:label-list'
    create_page = 'tasks:label-create'
    update_page = 'tasks:label-update'
    update_args = {'name': 'My label'}
    delete_page = 'tasks:label-delete'
    kwargs = {'pk': 4}
    model = Label

    def test_update(self):
        instances = super().test_update()
        self.assertEqual(instances.get(pk=self.kwargs['pk']).name, 'My label')
