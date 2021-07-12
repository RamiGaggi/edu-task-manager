release: python manage.py migrate
(cd tasks/; django-admin compilemessages)
web: gunicorn task_manager_site.wsgi --log-file -