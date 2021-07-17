from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext as _


def my_get_login_url(self):
    """Add denied_message."""
    login_url = self.login_url or settings.LOGIN_URL
    if not login_url:
        raise ImproperlyConfigured(
            '{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL, or override '
            '{0}.get_login_url().'.format(self.__class__.__name__)
        )

    denied_message = 'Вы не авторизованы! Пожалуйста, выполните вход.'
    messages.add_message(self.request, messages.ERROR, _(denied_message))

    return str(login_url)
