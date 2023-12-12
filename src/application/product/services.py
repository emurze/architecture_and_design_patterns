from domain.product import BaseProduct


class Product(BaseProduct):
    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    def get_title(self):
        return f'{self.class_name}'


class Banana(Product):
    pass


class WaterMelon(Product):
    pass


class Apple(Product):
    title: str = 'apple'

    def get_title(self) -> str:
        return self.title


class Melon(Product):
    title: str = 'apple'

    def get_title(self) -> str:
        return self.title
