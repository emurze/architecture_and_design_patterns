

install:
	poetry install


run:
	poetry run python3 src/main.py


test:
	poetry run pytest tests
