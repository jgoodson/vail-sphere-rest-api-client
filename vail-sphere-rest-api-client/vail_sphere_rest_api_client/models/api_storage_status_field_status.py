from enum import Enum


class ApiStorageStatusFieldStatus(str, Enum):
    DEGRADED = "degraded"
    DELETING = "deleting"
    OK = "ok"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
