import abc

from bounded_context.builders.house_builders import HouseBuilder
from bounded_context.entities.house import House


class BaseHouseDirector(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def construct(builder: HouseBuilder) -> House:
        ...
