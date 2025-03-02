from domain.student import Student
from infrastructure.repository.shared.base_repository import BaseRepository


class StudentRepository(BaseRepository[Student]):
    def __init__(self) -> None:
        super().__init__()

    def create(self, name: str, age: int, grade: str) -> Student:
        student = Student(name, age, grade)
        return self.add(student)
