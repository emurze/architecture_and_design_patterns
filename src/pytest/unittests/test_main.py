import pytest

from src.pytest.main import User


@pytest.mark.usefixtures("empty_users")
class TestUser:
    def test_can_create_1_user(self, user: User) -> None:
        print("<< Running 1 test >>")
        assert 1 == 1

    def test_can_create_2_user(self, user: User) -> None:
        print("<< Running 2 test >>")
        assert 2 == 2

    def test_can_create_3_user(self, user: User) -> None:
        print("<< Running 3 test >>")
        assert 3 == 3

    def test_can_create_4_user(self, user: User) -> None:
        print("<< Running 4 test >>")
        assert 4 == 4
