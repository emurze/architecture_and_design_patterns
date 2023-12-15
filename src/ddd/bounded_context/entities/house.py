from dataclasses import dataclass


@dataclass
class House:
    name: str
    price: float
    weight: float | None = None
    color: str | None = None
