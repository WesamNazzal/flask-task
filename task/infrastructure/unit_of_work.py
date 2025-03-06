from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from infrastructure.database.connection.database import engine


class UnitOfWork:
    def __init__(self):
        self.connection: Connection = engine.connect()
        self.transaction = self.connection.begin()

    def commit(self):
        try:
            self.transaction.commit()
        except Exception as e:
            self.transaction.rollback()
            raise e

    def rollback(self):
        self.transaction.rollback()

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()
