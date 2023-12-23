import copy
from dataclasses import dataclass
from datetime import date

from src.clean_architecture.model import OrderLine, Batch

today = date.today


def make_batch_and_line(
    stu: str, batch_qty: int, line_qty: int
) -> tuple[Batch, OrderLine]:
    return (
        Batch(ref=1, purchased_quantity=batch_qty, stu=stu, eta=today()),
        OrderLine(order_id=1, quantity=line_qty, stu=stu),
    )


def test_can_reduce_quantity() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=4)
    assert batch.can_allocate(line)


def test_cannot_allocate_when_repeatable_lines_go_to_a_single_batch() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=4)
    batch.allocate(line)
    line2 = OrderLine(order_id=2, stu="Melon", quantity=1)
    assert batch.can_allocate(line2) is False


def test_can_allocate_if_available_quantity_greater_than_required() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=4)
    assert batch.can_allocate(line)


def test_can_allocate_if_available_quantity_equal_to_required() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=5)
    assert batch.can_allocate(line)


def test_cannot_allocate_if_available_quantity_smaller_than_required() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=7)
    assert batch.can_allocate(line) is False


def test_cannot_allocate_if_sku_do_not_match() -> None:
    batch = Batch(ref=1, purchased_quantity=5, stu="Melon", eta=today())
    line = OrderLine(order_id=1, quantity=4, stu="Apple")
    assert batch.can_allocate(line) is False


def test_can_deallocate_allocated_line() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=4)
    batch.allocate(line)
    assert batch.can_deallocate(line)


def test_cannot_deallocate_unallocated_line() -> None:
    batch, line = make_batch_and_line(stu="Melon", batch_qty=5, line_qty=4)
    assert batch.can_deallocate(line) is False


def test_equal() -> None:
    batch = Batch(ref=1, purchased_quantity=12, stu="Melon", eta=today())
    batch2 = copy.copy(batch)
    batch2.stu = "Melon2"
    assert batch == batch2


def test_hashable() -> None:
    _ = {Batch(ref=1, purchased_quantity=12, stu="Melon", eta=today())}