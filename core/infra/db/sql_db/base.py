from datetime import datetime

from sqlalchemy import Column, DateTime, func, Integer
from sqlalchemy.orm import MappedColumn, mapped_column, DeclarativeBase, Mapped


class Base(DeclarativeBase):
    ...


class SQLBaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: MappedColumn[datetime] = Column(DateTime, server_default=func.now())
    updated_at: MappedColumn[datetime] = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
