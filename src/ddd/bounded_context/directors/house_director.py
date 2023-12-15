from dataclasses import dataclass

from bounded_context.builders.house_builders import HouseBuilder
from bounded_context.directors.interface import BaseHouseDirector
from bounded_context.entities.house import House


class StandardHouseDirector(BaseHouseDirector):
    @staticmethod
    def construct(builder: HouseBuilder) -> House:
        builder.set_name("best")
        builder.set_price(123)
        return builder.build()


class LargeHouseDirector(BaseHouseDirector):
    @staticmethod
    def construct(builder: HouseBuilder) -> House:
        builder.set_name("best")
        builder.set_price(123)
        builder.set_color("red")
        builder.set_weight(24.5)
        return builder.build()
