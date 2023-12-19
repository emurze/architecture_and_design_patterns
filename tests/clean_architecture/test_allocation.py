from datetime import date

from src.clean_architecture.model import OrderLine, Batch


def make_batch_and_line(
    stu: str, batch_qty: int, line_qty: int
) -> tuple[Batch, OrderLine]:
    """
    Make a Batch and an OrderLine instances for testing
    """
    return (
        Batch(batch_id=1, quantity=batch_qty, stu=stu, eta=date.today()),
        OrderLine(order_id=1, quantity=line_qty, stu=stu),
    )


def test_batch_reduced_quantity() -> None:
    """
    DI-Container - Low-level module
    """
    batch, order_line = make_batch_and_line(
        stu="Melon", batch_qty=5, line_qty=4
    )
    batch.allocate(order_line)

    assert batch.quantity == 1


def test_suppress_repeatable_order_lines_to_single_batch() -> None:
    """
    DI-Container - Low-level module
    """
    batch, order_line = make_batch_and_line(
        stu="Melon", batch_qty=5, line_qty=4
    )
    order_line2 = OrderLine(order_id=2, stu="Melon", quantity=1)
    batch.allocate(order_line)
    batch.allocate(order_line2)

    assert batch.quantity == 1


def test_ignore_negative_allocations() -> None:
    """
    DI-Container - Low-level module
    """
    batch, order_line = make_batch_and_line(
        stu="Melon", batch_qty=5, line_qty=6
    )
    batch.allocate(order_line)

    assert batch.quantity == 5

    order_line2 = OrderLine(stu="Melon", order_id=2, quantity=2)
    batch.allocate(order_line2)

    assert batch.quantity == 3
