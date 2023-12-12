import decimal
from _decimal import Decimal
from dataclasses import dataclass, field

from domain.product import BaseProduct


@dataclass
class Client:
    money: decimal = Decimal(0)
    products: list[BaseProduct] = field(default_factory=list)
