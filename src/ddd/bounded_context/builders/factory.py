from bounded_context.builders.house_builders import HouseBuilder
from bounded_context.entities.house import House


class HouseBuilderFactory:
    @staticmethod
    def get_builder(house: House) -> HouseBuilder:
        return HouseBuilder(house)
