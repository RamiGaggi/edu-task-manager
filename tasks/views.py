from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


def index(request):
    """Index page."""
    return render(request, 'tasks/index.html')


def login(request):
    """Index page."""
    return HttpResponse('!!!!!!')


class UserListView(ListView):
    template_name = 'tasks/user_list.html'
    model = User


class UserCreateView(CreateView):
    template_name = 'tasks/user_create.html'
    model = User
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
    ]

    def get_success_url(self):
        """Get url after registration."""
        return reverse('tasks:user-login')


class UserLoginView(CreateView):
    template_name = 'tasks/user_login.html'
    model = User
    fields = [
        'username',
        'password',
    ]

    def get_success_url(self):
        """Get url after registration."""
        return reverse('tasks:user-login')
