from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import mapper

import model


metadata = MetaData()

order_line = Table(
    "order_line",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String),
    Column("quantity", Integer),
    Column("order_id", Integer),
)


def start_mappers():
    line_mapper = mapper(model.OrderLine, order_line)
    return line_mapper
