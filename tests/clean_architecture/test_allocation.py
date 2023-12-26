from datetime import date, timedelta

import pytest

from src.clean_architecture.exceptions import OutOfStock
from src.clean_architecture.model import Batch, allocate, OrderLine

today = date.today()
tomorrow = today + timedelta(days=1)
later = today + timedelta(days=10)


def test_can_return_allocate_batch_ref() -> None:
    batch = Batch(ref=1, purchased_quantity=12, sku="Melon", eta=today)
    line = OrderLine(order_id=1, quantity=10, sku="Melon")
    allocation = allocate(line, [batch])
    assert allocation == batch.ref


def test_can_allocate_earliest_batch() -> None:
    batch1 = Batch(ref=1, purchased_quantity=12, sku="Melon", eta=today)
    batch2 = Batch(ref=1, purchased_quantity=12, sku="Melon", eta=tomorrow)
    batch3 = Batch(ref=1, purchased_quantity=12, sku="Melon", eta=later)
    line = OrderLine(order_id=1, quantity=10, sku="Melon")
    allocate(line, [batch2, batch3, batch1])

    assert batch1.available_quantity == 2
    assert batch2.available_quantity == 12
    assert batch3.available_quantity == 12


def test_prefer_stock_in_batches_to_shipments() -> None:
    stock_batch = Batch(ref=1, purchased_quantity=12, sku="M", eta=None)
    shipping_batch = Batch(ref=1, purchased_quantity=12, sku="M", eta=tomorrow)
    line = OrderLine(order_id=1, quantity=2, sku="M")
    allocate(line, [shipping_batch, stock_batch])

    assert stock_batch.available_quantity == 10
    assert shipping_batch.available_quantity == 12


def test_no_acceptable_batches_error() -> None:
    stock_batch = Batch(ref=1, purchased_quantity=12, sku="M", eta=None)
    shipping_batch = Batch(ref=1, purchased_quantity=12, sku="M", eta=tomorrow)
    line = OrderLine(order_id=1, quantity=20, sku="M")

    with pytest.raises(OutOfStock, match="M"):
        allocate(line, [shipping_batch, stock_batch])
