from typing import Any, Dict, List, Optional

from domain.student import Student
from infrastructure.repository.student_repository import StudentRepository


class StudentService:
    repo = StudentRepository()

    @staticmethod
    def get_all_students() -> List[Student]:
        return StudentService.repo.get_all()

    @staticmethod
    def get_student(student_id: int) -> Optional[Student]:
        return StudentService.repo.get(student_id)

    @staticmethod
    def create_student(name: str, age: int, grade: str) -> Student:
        return StudentService.repo.create(name, age, grade)

    @staticmethod
    def update_student(student_id: int, data: Dict[str, Any]) -> Optional[Student]:
        return StudentService.repo.update(student_id, data)

    @staticmethod
    def delete_student(student_id: int) -> bool:
        return StudentService.repo.delete(student_id)
