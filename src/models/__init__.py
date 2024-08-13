from .base import Base
from .data_point import DataPoint, DataType
from .data import DataStore
from sqlalchemy import Engine


table_objects = [
    DataPoint.__table__,
    DataStore.__table__
]


def setup_db(engine: Engine):
    Base.metadata.create_all(engine, tables=table_objects)
