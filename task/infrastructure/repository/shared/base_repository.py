from typing import Any, Dict, Generic, List, Optional, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.sql.schema import Table

from infrastructure.unit_of_work import UnitOfWork

T = TypeVar("T", bound=Table)


class BaseRepository(Generic[T]):
    def __init__(self, table: T):
        self.table: T = table

    def get_all(self) -> List[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(select(self.table)).fetchall()
            return [dict(row._mapping) for row in result] if result else []

    def get(self, record_id: int) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c.id == record_id)
            ).first()
            return dict(result._mapping) if result is not None else None

    def create(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            stmt = insert(self.table).values(**data).returning(self.table)
            result = uow.connection.execute(stmt).fetchone()
            return dict(result._mapping) if result is not None else None

    def update(self, record_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            stmt = (
                update(self.table)
                .where(self.table.c.id == record_id)
                .values(**data)
                .returning(self.table)
            )
            result = uow.connection.execute(stmt).fetchone()
            return dict(result._mapping) if result is not None else None

    def delete(self, record_id: int) -> bool:
        with UnitOfWork() as uow:
            stmt = delete(self.table).where(self.table.c.id == record_id)
            result = uow.connection.execute(stmt)
            return result.rowcount > 0
