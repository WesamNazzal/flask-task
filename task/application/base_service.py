from typing import Any, Dict, Generic, List, Tuple, TypeVar
from sqlalchemy.sql.schema import Table
from infrastructure.repository.shared.base_repository import BaseRepository

T = TypeVar('T', bound=Table)


class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repo = repository

    def get_all(self) -> Tuple[List[Dict[str, Any]], int]:
        return self.repo.get_all(), 200

    def get_by_id(self, record_id: int) -> Tuple[Dict[str, Any], int]:
        record = self.repo.get(record_id)
        if record is None:
            return {'error': 'Not found'}, 404
        return record, 200

    def create(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        return self.repo.create(data), 201

    def update(self, record_id: int, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        record = self.repo.update(record_id, data)
        if record is None:
            return {'error': 'Not found'}, 404
        return record, 200

    def delete(self, record_id: int) -> Tuple[Dict[str, Any], int]:
        return ({}, 204) if self.repo.delete(record_id) else ({'error': 'Not found'}, 404)
