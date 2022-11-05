install: # install poetry
	poetry install

pytest:
	poetry run pytest

lint: # запуск flake8 на проект python-project-50
	poetry run flake8

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml