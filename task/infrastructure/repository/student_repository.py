from sqlalchemy.sql.schema import Table

from infrastructure.database.schema.tables import student_table
from infrastructure.repository.shared.base_repository import BaseRepository


class StudentRepository(BaseRepository[Table]):
    def __init__(self) -> None:
        super().__init__(student_table)
