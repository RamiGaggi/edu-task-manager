from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext as _
from django.shortcuts import redirect
import functools


def add_denied_message_and_redirect(get):
    @functools.wraps(get)
    def wrapper(self, request, *args, **kwargs):
        get(self, request, *args, **kwargs)
        denied_message = _('У вас нет прав для изменения другого пользователя!')
        messages.add_message(self.request, messages.ERROR, denied_message)
        return redirect('tasks:user-list')
    return wrapper