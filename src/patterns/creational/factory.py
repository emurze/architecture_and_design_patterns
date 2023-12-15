import abc
from _decimal import Decimal
from dataclasses import dataclass


@dataclass
class Client:
    name: str
    money: Decimal


class BaseClientFactory(abc.ABC):
    @abc.abstractmethod
    def get_client(self) -> Client:
        ...


class EmptyClientFactory(BaseClientFactory):
    def get_client(self) -> Client:
        return Client(name="", money=Decimal(0))


class StandardClientFactory(BaseClientFactory):
    def get_client(self) -> Client:
        return Client(name="Client1", money=Decimal(100))


class PremiumClientFactory(BaseClientFactory):
    def get_client(self) -> Client:
        return Client(name="Client10", money=Decimal(10_000))


# OR
#
# Minuses:
#     - hardcode to strings
#     - OCP violation
#
#
# def Factory(string: str) -> Client:
#     clients = {
#         'empty': Client(name='', money=Decimal(0)),
#         'standard': Client(name='Client1', money=Decimal(100)),
#         'premium': Client(name='Client10', money=Decimal(10_000)),
#     }
#     return clients[string]


# OR More rarely example


class BaseProduct(abc.ABC):
    @abc.abstractmethod
    def operation(self) -> str:
        ...


class ProductA(BaseProduct):
    def operation(self) -> str:
        return "ProductA operation"


class ProductB(BaseProduct):
    def operation(self) -> str:
        return "ProductB operation"


class ProductC(BaseProduct):
    def operation(self) -> str:
        return "ProductC operation"


class BaseProductFactory(abc.ABC):
    @abc.abstractmethod
    def get_product(self) -> BaseProduct:
        ...


class ProductAFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return ProductA()


class ProductBFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return ProductB()


class ProductCFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return ProductC()
