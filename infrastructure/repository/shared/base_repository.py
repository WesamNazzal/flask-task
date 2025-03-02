from typing import Any, Dict, Generic, List, Optional, TypeVar

from domain.shared.base_entity import BaseEntity

T = TypeVar("T", bound="BaseEntity")


class BaseRepository(Generic[T]):
    def __init__(self) -> None:
        self.storage: Dict[int, T] = {}

    def add(self, obj: T) -> T:
        self.storage[obj.id] = obj
        return obj

    def get_all(self) -> List[T]:
        return list(self.storage.values())

    def get(self, obj_id: int) -> Optional[T]:
        return self.storage.get(obj_id)

    def update(self, obj_id: int, data: Dict[str, Any]) -> Optional[T]:
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            return obj
        return None

    def delete(self, obj_id: int) -> bool:
        return self.storage.pop(obj_id, None) is not None
