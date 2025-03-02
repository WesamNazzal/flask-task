from typing import Optional, Tuple

from flask import Response, jsonify, request
from flask.views import MethodView

from application.student_service import StudentService


class StudentAPI(MethodView):
    def get(self, student_id: Optional[int] = None) -> Tuple[Response, int]:
        response, status = StudentService.get_all_students() if student_id is None else StudentService.get_student(student_id)
        return jsonify(response), status

    def post(self) -> Tuple[Response, int]:
        data = request.get_json()
        response, status = StudentService.create_student(data)
        return jsonify(response), status

    def patch(self, student_id: int) -> Tuple[Response, int]:
        data = request.get_json()
        response, status = StudentService.update_student(student_id, data)
        return jsonify(response), status

    def delete(self, student_id: int) -> Tuple[Response, int]:
        response, status = StudentService.delete_student(student_id)
        return jsonify(response), status
