from dataclasses import dataclass

from bounded_context.entities.house import House


@dataclass
class HouseBuilder:
    house: House

    def set_name(self, name: str) -> "HouseBuilder":
        self.house.name = name
        return self

    def set_price(self, price: int) -> "HouseBuilder":
        self.house.price = price
        return self

    def set_weight(self, weight: float) -> "HouseBuilder":
        self.house.weight = weight
        return self

    def set_color(self, color: str) -> "HouseBuilder":
        self.house.color = color
        return self

    def build(self) -> House:
        return self.house
