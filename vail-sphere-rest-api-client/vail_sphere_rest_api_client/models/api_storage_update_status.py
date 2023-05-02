from enum import Enum


class ApiStorageUpdateStatus(str, Enum):
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)
