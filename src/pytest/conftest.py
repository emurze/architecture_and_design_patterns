from typing import Generator

import pytest


# Fixture can contain only 1 yield
# "session" "package" "module" "class" "function"


@pytest.fixture(scope="session", autouse=True)
def setup_db() -> Generator:
    print("\n<< Creating database ... >>")
    yield
    print("<< Dropping database ... >>")
