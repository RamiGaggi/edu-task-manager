install:
	@poetry install --extras psycopg2-binary

build:
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest

lint:
	poetry run flake8