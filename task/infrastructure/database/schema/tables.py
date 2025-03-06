from sqlalchemy import Column, Integer, String, Table

from infrastructure.database.connection.database import metadata

student_table = Table(
    'students',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('age', Integer, nullable=False),
    Column('grade', String(50), nullable=False),
)
