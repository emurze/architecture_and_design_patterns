import copy
from datetime import date

from src.clean_architecture.model import OrderLine, Batch

today = date.today


def make_batch_and_copy(sku: str, batch_qty: int) -> tuple[Batch, Batch]:
    batch = Batch(ref=1, purchased_quantity=batch_qty, sku=sku, eta=today())
    return batch, copy.copy(batch)


def make_batch_and_line(
    sku: str, batch_qty: int, line_qty: int
) -> tuple[Batch, OrderLine]:
    return (
        Batch(ref=1, purchased_quantity=batch_qty, sku=sku, eta=today()),
        OrderLine(order_id=1, quantity=line_qty, sku=sku),
    )


def test_can_reduce_quantity() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=4)
    assert batch.can_allocate(line)


def test_cannot_allocate_when_repeatable_lines_go_to_a_single_batch() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=4)
    batch.allocate(line)
    line2 = OrderLine(order_id=2, sku="Melon", quantity=1)
    assert batch.can_allocate(line2) is False


def test_can_allocate_if_available_quantity_greater_than_required() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=4)
    assert batch.can_allocate(line)


def test_can_allocate_if_available_quantity_equal_to_required() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=5)
    assert batch.can_allocate(line)


def test_cannot_allocate_if_available_quantity_smaller_than_required() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=7)
    assert batch.can_allocate(line) is False


def test_cannot_allocate_if_sku_do_not_match() -> None:
    batch = Batch(ref=1, purchased_quantity=5, sku="Melon", eta=today())
    line = OrderLine(order_id=1, quantity=4, sku="Apple")
    assert batch.can_allocate(line) is False


def test_can_deallocate_allocated_line() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=4)
    batch.allocate(line)
    assert batch.can_deallocate(line)


def test_cannot_deallocate_unallocated_line() -> None:
    batch, line = make_batch_and_line(sku="Melon", batch_qty=5, line_qty=4)
    assert batch.can_deallocate(line) is False


def test_equal() -> None:
    batch, batch2 = make_batch_and_copy(sku="Melon", batch_qty=12)
    batch2.sku = "Melon2"
    assert batch == batch2


def test_hashable() -> None:
    _ = {Batch(ref=1, purchased_quantity=12, sku="Melon", eta=today())}
