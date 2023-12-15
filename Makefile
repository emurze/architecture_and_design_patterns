

install:
	poetry install --no-root

	git init

	touch .git/hooks/pre-commit

	chmod +x .git/hooks/pre-commit

	echo '''        \
	#!/bin/sh       \
				    \
	make black &&   \
	                \
	git add . &&    \
	                \
	make test;      \
	''' > .git/hooks/pre-commit

run:
	poetry run python3 src/main.py

black:
	poetry run black .

lint:
	poetry run

types:
	poetry run mypy tests src

test:
	poetry run pytest tests src
