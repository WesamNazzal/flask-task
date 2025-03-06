from infrastructure.repository.shared.base_repository import BaseRepository
from infrastructure.database.schema.tables import student_table

class StudentRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(student_table)

    