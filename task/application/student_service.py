from typing import Any, Dict, Tuple
from application.base_service import BaseService
from infrastructure.repository.student_repository import StudentRepository
from sqlalchemy.sql.schema import Table

class StudentService(BaseService[Table]):
    def __init__(self) -> None:
        super().__init__(StudentRepository())  

    def create_student(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        created_record = self.create(data)
        if created_record is None: 
            return {'error': 'Failed to create student'}, 500
        return created_record, 201  
