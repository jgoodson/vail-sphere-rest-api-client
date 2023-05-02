from enum import Enum


class ApiDeleteStatusFieldStatus(str, Enum):
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)
