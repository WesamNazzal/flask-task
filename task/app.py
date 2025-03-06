from flask import Flask
from config import Config
from infrastructure.database.connection.database import engine, metadata
from presentation.student_route import StudentAPI

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    with engine.connect() as conn:
        metadata.create_all(engine)

student_view = StudentAPI.as_view('student_api')
app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
app.add_url_rule('/students/<int:student_id>', view_func=student_view, methods=['GET', 'PATCH', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
