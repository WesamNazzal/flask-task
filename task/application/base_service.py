from typing import Any, Dict, List, Tuple
from infrastructure.repository.shared.base_repository import BaseRepository
class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repo = repository()

    def get_all(self) -> Tuple[List[Dict[str, Any]], int]:
        return self.repo.get_all(), 200

    def get_by_id(self, record_id: int) -> Tuple[Dict[str, Any], int]:
        record = self.repo.get(record_id)
        return (record, 200) if record else ({'error': 'Not found'}, 404)

    def create(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        return self.repo.create(data), 201

    def update(self, record_id: int, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        record = self.repo.update(record_id, data)
        return (record, 200) if record else ({'error': 'Not found'}, 404)

    def delete(self, record_id: int) -> Tuple[Dict[str, Any], int]:
        return ({}, 204) if self.repo.delete(record_id) else ({'error': 'Not found'}, 404)
