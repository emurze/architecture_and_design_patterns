import abc


class BaseProduct(abc.ABC):
    @abc.abstractmethod
    def get_title(self) -> str: ...


class BaseProductFactory(abc.ABC):
    @abc.abstractmethod
    def get_product(self) -> BaseProduct: ...
