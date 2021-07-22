release: python manage.py make migrations && python manage.py migrate
web: gunicorn task_manager.wsgi --log-file -