from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import Model
from django.urls import reverse


class TaskMixinTest:
    def setUp(self):
        self.login = self.client.post(
            reverse(self.user_login_page),
            self.credentials,
        )

    fixtures = ['data.json']

    reg_info = {
        'first_name': 'test3',
        'last_name': 'test3',
        'username': 'test3',
        'password1': 'xcCC_123f5',
        'password2': 'xcCC_123f5',
    }
    credentials = {
        'username': 'test1',
        'password': 'http://localhost:8000/',
    }
    index_page = 'tasks:index'
    user_login_page = 'tasks:user-login'

    list_page: str = ...
    create_page: str = ...
    update_page: str = ...
    update_args: dict = ...
    delete_page: str = ...
    kwargs: dict = ...
    model: Model = ...

    def get_objects(self, model):
        return model.objects.all()

    def get_check_page(self, url, status_code=200):
        response = self.client.get(url)  # noqa: WPS204 Overused expression
        return self.assertEqual(response.status_code, status_code)

    def test_list(self):
        url = reverse(self.list_page)
        self.get_check_page(url)

    def test_update(self):
        url_update = reverse(self.update_page, kwargs=self.kwargs)
        self.client.post(url_update, self.update_args)
        return self.get_objects(self.model)

    def test_delete(self):
        url_delete = reverse(self.delete_page, kwargs=self.kwargs)
        self.get_check_page(url_delete)
        self.client.post(url_delete, kwargs=self.kwargs)

        instances = self.get_objects(self.model)
        with self.assertRaises(ObjectDoesNotExist):
            instances.get(pk=self.kwargs['pk'])
