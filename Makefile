

make install:
	poetry install


make run:
	poetry run python3 src/main.py


make test:
	poetry run pytest tests
