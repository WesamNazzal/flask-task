from typing import Optional, Type

from sqlalchemy.engine import Connection

from infrastructure.database.connection.database import engine


class UnitOfWork:
    def __init__(self) -> None:
        self.connection: Connection = engine.connect()
        self.transaction = self.connection.begin()

    def commit(self) -> None:
        try:
            self.transaction.commit()
        except Exception as e:
            self.transaction.rollback()
            raise e

    def rollback(self) -> None:
        self.transaction.rollback()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> 'UnitOfWork':
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[object]) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()
