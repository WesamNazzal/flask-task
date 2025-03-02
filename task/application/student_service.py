from typing import Any, Dict, List, Tuple

from infrastructure.repository.student_repository import StudentRepository


class StudentService:
    repo = StudentRepository()

    @staticmethod
    def get_all_students() -> Tuple[List[Dict[str, Any]], int]:
        students = [student.__dict__ for student in StudentService.repo.get_all()]
        return students, 200

    @staticmethod
    def get_student(student_id: int) -> Tuple[Dict[str, Any], int]:
        student = StudentService.repo.get(student_id)
        if not student:
            return {"error": "Student not found"}, 404
        return student.__dict__, 200

    @staticmethod
    def create_student(data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        if not all(k in data for k in ('name', 'age', 'grade')):
            return {"error": "Missing required fields"}, 400

        student = StudentService.repo.create(data["name"], data["age"], data["grade"])
        return student.__dict__, 201

    @staticmethod
    def update_student(student_id: int, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        student = StudentService.repo.update(student_id, data)
        if not student:
            return {"error": "Student not found"}, 404
        return student.__dict__, 200

    @staticmethod
    def delete_student(student_id: int) -> Tuple[Dict[str, Any], int]:
        if not StudentService.repo.delete(student_id):
            return {"error": "Student not found"}, 404
        return {}, 204
