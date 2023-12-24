# Install

install:
	poetry install --no-root

	git init

	cp .github/hooks/pre-commit.sh .git/hooks/pre-commit

	chmod +x .git/hooks/pre-commit


# Lint

black:
	poetry run black -l 79 .


lint:
	poetry run flake8 --config setup.cfg tests src;


pip_lint:
	flake8 --config setup.cfg tests src;


types:
	poetry run mypy tests src


pip_check_types:
	mypy tests src


# Tests

coverage:
	poetry run coverage run src/main.py && poetry run coverage report


unittests:
	poetry run pytest -s tests


test: lint types unittests run


# Run

run:
	poetry run python3 src/main.py

