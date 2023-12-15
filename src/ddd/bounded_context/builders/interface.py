import abc

from bounded_context.entities.house import House


class BaseHouseBuilder(abc.ABC):
    @abc.abstractmethod
    def build(self) -> House:
        ...

    @abc.abstractmethod
    def set_name(self) -> "BaseHouseBuilder":
        ...
