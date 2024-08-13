from typing import Optional, Union

import uuid
import datetime

from sqlalchemy import DATE, TEXT, ForeignKey, FLOAT, BOOLEAN, String, UniqueConstraint, UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .data_point import DataPoint, DataType


DataReturnType = Union[str, float, datetime.date, bool]


class DataStore(Base):
    __tablename__ = 'data_store'
    __table_args__ = (
        UniqueConstraint('user_id', 'group_id', 'data_point_id'),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    data_point_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('data_point.id'))

    group_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID, default=uuid.uuid4, nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID, default=uuid.uuid4, nullable=True)

    text: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)
    number: Mapped[Optional[float]] = mapped_column(FLOAT, nullable=True)
    date: Mapped[Optional[datetime.date]] = mapped_column(DATE, nullable=True)
    boolean: Mapped[Optional[bool]] = mapped_column(BOOLEAN, nullable=True)

    def value(self, data_point: DataPoint) -> Optional[DataReturnType]:
        if data_point.data_type == DataType.number:
            return self.number
        
        if data_point.data_type == DataType.text:
            return self.text
        
        if data_point.data_type == DataType.date:
            return self.date
        
        if data_point.data_type == DataType.boolean:
            return self.boolean
        
        return None
