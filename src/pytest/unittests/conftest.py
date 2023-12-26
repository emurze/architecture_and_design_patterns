from datetime import date, timedelta

import pytest

from src.pytest.main import User


@pytest.fixture
def user() -> User:
    twenty_years_ago = date.today() - timedelta(days=365.25 * 20)
    return User(
        birthday=twenty_years_ago,
        first_name="John",
        last_name="Zamotevsky",
    )


@pytest.fixture
def empty_users() -> None:
    print("<< Empty users! >>")
