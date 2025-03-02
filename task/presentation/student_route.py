from typing import Dict, Optional, Tuple, Union

from flask import Response, jsonify, request
from flask.views import MethodView

from application.student_service import StudentService
from domain.student import Student


class StudentAPI(MethodView):
    def get(self, student_id: Optional[int] = None) -> Union[Tuple[Response, int], Dict[str, str]]:
        if student_id is None:
            students = StudentService.get_all_students()
            return jsonify([s.__dict__ for s in students]), 200

        student = StudentService.get_student(student_id)
        if student:
            return jsonify(student.__dict__), 200
        return jsonify({'error': 'Student not found'}), 404

    def post(self) -> Tuple[Response, int]:
        data = request.get_json()
        if not all(k in data for k in ('name', 'age', 'grade')):
            return jsonify({'error': 'Missing required fields'}), 400

        student: Student = StudentService.create_student(
            data['name'], data['age'], data['grade']
        )
        return jsonify(student.__dict__), 201

    def patch(self, student_id: int) -> Union[Tuple[Response, int], Dict[str, str]]:  # ✅ Changed from put to patch
        data = request.get_json()
        student: Optional[Student] = StudentService.update_student(student_id, data)
        if student:
            return jsonify(student.__dict__), 200
        return jsonify({'error': 'Student not found'}), 404

    def delete(self, student_id: int) -> Tuple[Response, int]:
        if StudentService.delete_student(student_id):
            return jsonify({}), 204
        return jsonify({'error': 'Student not found'}), 404
