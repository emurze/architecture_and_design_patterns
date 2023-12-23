from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True)
class OrderLine:
    """
    Value object is object that identified by data and is immutable
    """

    order_id: int
    stu: str
    quantity: int


@dataclass
class Batch:
    ref: int
    stu: str
    eta: date
    purchased_quantity: int
    _allocations: set[OrderLine] = field(
        default_factory=set,
        repr=False,
        init=False,
    )

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine) -> None:
        if self.can_deallocate(line):
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self.purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return (
            self.available_quantity >= line.quantity
            and self.stu == line.stu
            and not self._allocations
        )

    def can_deallocate(self, line: OrderLine) -> bool:
        return line in self._allocations
