from dataclasses import dataclass

from domain.product import BaseProduct
from entities.client import Client


@dataclass(frozen=True, eq=True)
class ShopService:
    client: Client

    def buy(self, product: BaseProduct):
        self.client.products.append(product)
