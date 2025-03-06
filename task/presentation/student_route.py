from flask.views import MethodView
from flask import request, jsonify
from application.student_service import StudentService

student_service = StudentService()

class StudentAPI(MethodView):

    def get(self, student_id=None):
        if student_id is None:
            return jsonify(student_service.get_all()[0]), 200
        return jsonify(student_service.get_by_id(student_id)[0]), student_service.get_by_id(student_id)[1]

    def post(self):
        return jsonify(student_service.create_student(request.json)[0]), student_service.create_student(request.json)[1]

    def patch(self, student_id):
        return jsonify(student_service.update(student_id, request.json)[0]), student_service.update(student_id, request.json)[1]

    def delete(self, student_id):
        return jsonify(student_service.delete(student_id)[0]), student_service.delete(student_id)[1]
