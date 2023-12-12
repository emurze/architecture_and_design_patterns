from application.product.services import Apple, Banana, WaterMelon, Melon
from domain.product import BaseProductFactory, BaseProduct


class AppleFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return Apple()


class BananaFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return Banana()


class MelonFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return Melon()


class WaterMelonFactory(BaseProductFactory):
    def get_product(self) -> BaseProduct:
        return WaterMelon()


# As alternative

# Minuses:
#     - doesn't support long creating processes
#     - misunderstanding string instead of object requires Enum

# def ProductFactory(default="melon"):
#     products = {
#         'water_melon': WaterMelon,
#         'banana': Banana,
#         'melon': Melon,
#         'apple': Apple,
#     }
#     return products[default].get_product()

