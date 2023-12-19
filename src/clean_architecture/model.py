from dataclasses import dataclass, field
from datetime import date


@dataclass(eq=True, frozen=True)
class OrderLine:
    """
    High-level module
    """

    order_id: int
    quantity: int
    stu: str


@dataclass
class Batch:
    """
    High-level module
    """

    batch_id: int
    quantity: int
    stu: str
    eta: date
    __is_allocated: bool = field(
        default=False,
        repr=False,
        init=False,
        compare=False,
        kw_only=False,
    )

    def allocate(self, order_line: OrderLine) -> None:
        if not self.__is_allocated:
            remains = self.quantity - order_line.quantity

            if remains < 0:
                return

            self.quantity = remains
            self.__is_allocated = True
