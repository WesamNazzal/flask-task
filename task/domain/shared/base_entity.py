class BaseEntity:
    next_id: int = 1

    def __init__(self) -> None:
        self.id: int = BaseEntity.next_id
        BaseEntity.next_id += 1
