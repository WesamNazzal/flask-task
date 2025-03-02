from flask import Flask

from presentation.student_route import StudentAPI

app = Flask(__name__)

student_view = StudentAPI.as_view('student_api')

app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
app.add_url_rule('/students/<int:student_id>',
                 view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
