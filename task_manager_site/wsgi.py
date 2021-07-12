"""
WSGI config for task_manager_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from task_manager_site.settings import BASE_DIR
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_site.settings')

application = get_wsgi_application()

application = WhiteNoise(
    application,
    root=os.path.join(BASE_DIR, 'staticfiles'),
)
