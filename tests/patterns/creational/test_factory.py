from _decimal import Decimal

from src.patterns.creational.factory import (
    EmptyClientFactory,
    StandardClientFactory,
    PremiumClientFactory,
    ProductAFactory,
    ProductBFactory,
    ProductCFactory,
)


class TestClientFactories:
    @staticmethod
    def test_empty_client_factory() -> None:
        client = EmptyClientFactory().get_client()

        assert client.name == ""
        assert client.money == Decimal(0)

    @staticmethod
    def test_standard_client_factory() -> None:
        client = StandardClientFactory().get_client()

        assert client.name == "Client1"
        assert client.money == Decimal(100)

    @staticmethod
    def test_premium_client_factory() -> None:
        client = PremiumClientFactory().get_client()

        assert client.name == "Client10"
        assert client.money == Decimal(10_000)


class TestProductFactories:
    @staticmethod
    def test_product_a_factory() -> None:
        product = ProductAFactory().get_product()
        assert "ProductA operation" == product.operation()

    @staticmethod
    def test_product_b_factory() -> None:
        product = ProductBFactory().get_product()
        assert "ProductB operation" == product.operation()

    @staticmethod
    def test_product_c_factory() -> None:
        product = ProductCFactory().get_product()
        assert "ProductC operation" == product.operation()
