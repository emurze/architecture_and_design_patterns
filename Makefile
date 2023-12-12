

install:
	poetry install
	# Setup git hook


run:
	poetry run python3 src/main.py


lint:
	# Lint using black

test:
	poetry run pytest tests
