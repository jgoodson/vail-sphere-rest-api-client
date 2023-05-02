from enum import Enum


class ApiServiceStatus(str, Enum):
    OK = "ok"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
