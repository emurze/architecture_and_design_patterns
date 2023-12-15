# Install

install:
	poetry install --no-root

	git init

	echo '''           \
	#!/bin/sh          \
				       \
	make black &&      \
	                   \
	git add . &&       \
	                   \
	make test          \
	''' > .git/hooks/pre-commit

	chmod +x .git/hooks/pre-commit


# Lint

black:
	poetry run black .


lint:
	poetry run flake8 --config setup.cfg tests src;


pip_lint:
	flake8 --config setup.cfg tests src;


types:
	poetry run mypy tests src


pip_types:
	mypy tests src


# Tests

coverage:
	poetry run coverage run src/main.py && poetry run coverage report


unittests:
	poetry run pytest tests


test: lint types coverage unittests run

# Run

run:
	poetry run python3 src/main.py

