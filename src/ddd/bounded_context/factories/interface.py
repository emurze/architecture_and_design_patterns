import abc

from bounded_context.entities.house import House


class BaseHouseFactory(abc.ABC):
    @abc.abstractmethod
    def get_house(self) -> House:
        ...
