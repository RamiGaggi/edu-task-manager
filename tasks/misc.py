from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.shortcuts import redirect
import functools
class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('tasks:user-login')
    
    def get_login_url(self):
        denied_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
        messages.add_message(self.request, messages.ERROR, denied_message)
        return super().get_login_url()

def add_denied_message_and_redirect(get):
    @functools.wraps(get)
    def wrapper(self, request, *args, **kwargs):
        get(self, request, *args, **kwargs)
        denied_message = _('У вас нет прав для изменения другого пользователя!')
        messages.add_message(self.request, messages.ERROR, denied_message)
        return redirect('tasks:user-list')
    return wrapper