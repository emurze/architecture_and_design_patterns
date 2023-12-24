from dataclasses import dataclass, field
from datetime import date
from typing import NoReturn

from src.clean_architecture.exceptions import OutOfStock


@dataclass(frozen=True)
class OrderLine:
    """
    Value object is object that identified by data (order_id, stu, quantity),
    haven't a long-lived identity (id, ref), and is immutable.
    Because if I change a property then I will get a new value object.
    Statement (frozen=True) means that the entire class will have __eq__ and
    __hash__ methods and will be immutable.
    """

    order_id: int  # order_id is for another Object
    stu: str
    quantity: int


@dataclass
class Batch:
    """
    Entity is object that has long-lived identity and is mutable.
    If we change Entity then get the same Entity with changed properties.
    If you want to use Entity in set or dict key then you should implement
    __eq__ and __hash__ methods for identification attribute like ref, id, uuid
    """

    ref: int
    stu: str
    purchased_quantity: int
    eta: date | None = None
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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Batch):
            return False
        else:
            return self.ref == other.ref

    def __gt__(self, other: object) -> bool:
        """If False then to more priority"""
        if self.eta is None:
            return False
        if (other_eta := getattr(other, "eta")) is None:
            return True
        return self.eta > other_eta

    def __hash__(self) -> int:
        return hash(self.ref)


def allocate(line: OrderLine, batches: list[Batch]) -> NoReturn | int:
    """
    Allocate only first batch that can allocate for line
    """
    try:
        earliest_acceptable_batch = next(
            b for b in sorted(batches) if b.can_allocate(line)
        )
    except StopIteration:
        raise OutOfStock(f"Our batches haven't so big amount of {line.stu}")
    else:
        earliest_acceptable_batch.allocate(line)
        return earliest_acceptable_batch.ref
