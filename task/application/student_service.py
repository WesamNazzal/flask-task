from typing import Any, Dict, Tuple
from application.base_service import BaseService
from infrastructure.repository.student_repository import StudentRepository
class StudentService(BaseService):
    def __init__(self):
        super().__init__(StudentRepository)

    def create_student(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        if not all(k in data for k in ('name', 'age', 'grade')):
            return {'error': 'Missing required fields'}, 400
        return self.create(data)
