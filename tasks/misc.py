import functools

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('tasks:user-login')

    def get_login_url(self):  # noqa: WPS615
        denied_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
        messages.add_message(self.request, messages.ERROR, denied_message)
        return super().get_login_url()


def add_denied_message_and_redirect(redirect_url=None, message=None):
    def decorator(get):
        @functools.wraps(get)
        def wrapper(self, request, *args, **kwargs):
            response = get(self, request, *args, **kwargs)
            if response:
                return response
            messages.add_message(self.request, messages.ERROR, message)
            return redirect(redirect_url)
        return wrapper
    return decorator
