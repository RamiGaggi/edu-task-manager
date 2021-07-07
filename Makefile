install:
	poetry install --extras psycopg2-binary

runserver:
	poetry run python manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8

check:
	poetry run python -m task_manager.settings
test:
	poetry run pytest

test-coverage:
	poetry run pytest

