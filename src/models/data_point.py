import enum
from typing import Optional
import uuid

from sqlalchemy import Enum, String, UniqueConstraint, UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class DataType(enum.Enum):
    number = 1
    text = 2
    date = 3
    boolean = 4


class DataPoint(Base):
    __tablename__ = 'data_point'
    __table_args__ = (
        UniqueConstraint('code'),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    data_type: Mapped[DataType] = mapped_column(Enum(DataType), nullable=False)
    code: Mapped[str] = mapped_column(String(10))
    name: Mapped[Optional[str]] = mapped_column(String(125), nullable=True)
