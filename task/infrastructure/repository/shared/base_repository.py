from typing import Any, Dict, List, Optional
from sqlalchemy import select, insert, update, delete
from sqlalchemy.sql.schema import Table
from infrastructure.unit_of_work import UnitOfWork


class BaseRepository:
    def __init__(self, table: Table):
        self.table = table

    def get_all(self) -> List[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(select(self.table)).fetchall()
            return [dict(row._mapping) for row in result]

    def get(self, record_id: int) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            result = uow.connection.execute(
                select(self.table).where(self.table.c.id == record_id)
            ).first()
            return dict(result._mapping) if result else None

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        with UnitOfWork() as uow:
            stmt = insert(self.table).values(**data).returning(self.table)
            result = uow.connection.execute(stmt)
            return dict(result.fetchone()._mapping)

    def update(self, record_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        with UnitOfWork() as uow:
            stmt = (
                update(self.table)
                .where(self.table.c.id == record_id)
                .values(**data)
                .returning(self.table)
            )
            result = uow.connection.execute(stmt)
            return dict(result.fetchone()._mapping) if result.rowcount > 0 else None

    def delete(self, record_id: int) -> bool:
        with UnitOfWork() as uow:
            stmt = delete(self.table).where(self.table.c.id == record_id)
            result = uow.connection.execute(stmt)
            return result.rowcount > 0
