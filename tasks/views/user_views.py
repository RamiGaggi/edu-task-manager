from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tasks.forms import UserRegistrationForm
from tasks.misc import MyLoginRequiredMixin, add_denied_message_and_redirect


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


class UserDeleteView(MyLoginRequiredMixin, DeleteView):
    model = User
    template_name = 'tasks/user_delete.html'
    success_url = reverse_lazy('tasks:user-list')

    @add_denied_message_and_redirect(
        redirect_url='tasks:user-list',
        message=_('У вас нет прав для изменения другого пользователя!'),
    )
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == self.kwargs.get('pk'):
            return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Add success message fo delete."""
        success_message = _('Пользователь успешно удалён')
        messages.add_message(self.request, messages.SUCCESS, _(success_message))
        return super().delete(request, *args, **kwargs)


class UserUpdateView(MyLoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'tasks/user_update.html'
    login_url = reverse_lazy('tasks:user-login')
    success_url = reverse_lazy('tasks:user-list')

    @add_denied_message_and_redirect(
        redirect_url='tasks:user-list',
        message=_('У вас нет прав для изменения другого пользователя!'),
    )
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == self.kwargs.get('pk'):
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Add success message for update."""
        success_message = _('Пользователь успешно изменён')
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)
