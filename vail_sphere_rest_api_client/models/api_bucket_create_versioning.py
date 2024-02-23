from enum import Enum


class ApiBucketCreateVersioning(str, Enum):
    ENABLED = "Enabled"
    SUSPENDED = "Suspended"
    DISABLED = ""

    def __str__(self) -> str:
        return str(self.value)
