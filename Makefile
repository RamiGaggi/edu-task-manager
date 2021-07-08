install:
	poetry install --extras psycopg2-binary

runserver:
	poetry run python manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8

check:
	poetry run python -m task_manager_site.settings

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test

coverage-xml:
	poetry run coverage xml

requirements.txt: poetry.lock
	poetry export --format requirements.txt --output requirements.txt --extras psycopg2
