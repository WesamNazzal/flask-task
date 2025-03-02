from domain.shared.base_entity import BaseEntity


class Student(BaseEntity):
    def __init__(self, name: str, age: int, grade: str) -> None:
        super().__init__()
        self.name: str = name
        self.age: int = age
        self.grade: str = grade
