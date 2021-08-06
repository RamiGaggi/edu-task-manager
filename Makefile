install:
	@poetry install

runserver:
	@poetry run python manage.py runserver 0.0.0.0:8000

migrations:
	@poetry run python manage.py makemigrations

migrate: migrations
	@poetry run python manage.py migrate

setup: migrate
	@echo Create a super user
	@poetry run python manage.py createsuperuser

lint:
	@poetry run flake8

check:
	@poetry run python -m task_manager.settings

secret-key:
	@poetry run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

test:
	@poetry run python manage.py test tasks

test-coverage:
	@poetry run coverage run manage.py test

coverage-xml:
	@poetry run coverage xml

requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt

collectstatic:
	@poetry run python manage.py collectstatic

messages:
	(cd tasks/; poetry run django-admin makemessages -l $(locale))


compile_translation: messages
	@(cd tasks/; poetry run django-admin compilemessages)

dump-data:
	@poetry run python manage.py dumpdata --indent 4 -e contenttypes -e auth.Permission -e sessions > tasks/fixtures/dump_data.json
