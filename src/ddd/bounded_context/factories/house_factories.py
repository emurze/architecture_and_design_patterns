from bounded_context.entities.house import House


class EmptyHouseFactory:
    @staticmethod
    def get_house() -> House:
        return House(name="", price=0)
