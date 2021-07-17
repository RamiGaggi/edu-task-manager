from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tasks.forms import UserRegistrationForm
from tasks.misc import my_get_login_url


class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class UserListView(ListView):
    context_object_name = 'user_list'
    template_name = 'tasks/user_list.html'
    model = User


class UserRegistrationView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'tasks/user_create.html'
    success_message = _('Пользователь успешно зарегистрирован')

    def get_success_url(self):
        """Get url after registration."""
        return reverse('tasks:user-login')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'tasks/user_login.html'
    model = User
    fields = [
        'username',
        'password',
    ]
    success_message = _('Вы залогинены')

    def get_success_url(self):
        """Get url after registration."""
        return reverse('tasks:index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('tasks:index')

    def dispatch(self, request, *args, **kwargs):
        """Override standart method to add message."""
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _('Вы разлогинены'))
        return response


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'tasks/user_delete.html'
    login_url = reverse_lazy('tasks:user-login')
    success_url = reverse_lazy('tasks:user-list')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if self.request.user.id == self.kwargs.get('pk'):
            return super().get(request, *args, **kwargs)
        denied_message = 'У вас нет прав для изменения другого пользователя!'
        messages.add_message(self.request, messages.ERROR, _(denied_message))
        return redirect('tasks:user-list')

    def get_login_url(self):  # noqa: WPS615
        """Add denied message message fot delete."""
        return my_get_login_url(self)

    def delete(self, request, *args, **kwargs):
        """Add success message fo delete."""
        success_message = _('Пользователь успешно удалён')
        messages.add_message(self.request, messages.SUCCESS, _(success_message))
        return super().delete(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'tasks/user_update.html'
    login_url = reverse_lazy('tasks:user-login')
    success_url = reverse_lazy('tasks:user-list')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if self.request.user.id == self.kwargs.get('pk'):
            return super().get(request, *args, **kwargs)
        denied_message = _('У вас нет прав для изменения другого пользователя!')
        messages.add_message(self.request, messages.ERROR, denied_message)
        return redirect('tasks:user-list')

    def get_login_url(self):  # noqa: WPS615
        """Add denied message message fot delete."""
        return my_get_login_url(self)

    def form_valid(self, form):
        """Add success message for update."""
        success_message = _('Пользователь успешно изменён')
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)
