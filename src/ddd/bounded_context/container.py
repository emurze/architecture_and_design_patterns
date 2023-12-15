from bounded_context.builders.factory import HouseBuilderFactory
from bounded_context.directors.house_director import StandardHouseDirector
from bounded_context.factories.house_factories import EmptyHouseFactory


class AppContainer:
    house_factory = EmptyHouseFactory

    builder_factory = HouseBuilderFactory

    director = StandardHouseDirector

    def run(self) -> None:
        temp_house = self.house_factory.get_house()
        house_builder = self.builder_factory.get_builder(temp_house)
        house = self.director.construct(house_builder)
        print(house)


if __name__ == "__main__":
    container = AppContainer()
    container.run()
