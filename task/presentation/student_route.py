from typing import Any, Dict, Optional, Tuple

from flask import jsonify, request
from flask.views import MethodView

from application.student_service import StudentService

student_service = StudentService()


class StudentAPI(MethodView):

    def get(self, student_id: Optional[int] = None) -> Tuple[Any, int]:
        if student_id is None:
            students, status_code = student_service.get_all()
            return jsonify(students), status_code
        student, status_code = student_service.get_by_id(student_id)
        return jsonify(student), status_code

    def post(self) -> Tuple[Any, int]:
        data: Optional[Dict[str, Any]] = request.get_json()
        if not isinstance(data, dict):
            return jsonify({'error': 'Invalid input'}), 400
        student, status_code = student_service.create_student(data)
        return jsonify(student), status_code

    def patch(self, student_id: int) -> Tuple[Any, int]:
        data: Optional[Dict[str, Any]] = request.get_json()
        if not isinstance(data, dict):
            return jsonify({'error': 'Invalid input'}), 400
        updated_student, status_code = student_service.update(student_id, data)
        return jsonify(updated_student), status_code

    def delete(self, student_id: int) -> Tuple[Any, int]:
        response, status_code = student_service.delete(student_id)
        return jsonify(response), status_code
