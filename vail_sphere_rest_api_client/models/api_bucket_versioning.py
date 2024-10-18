from enum import Enum


class ApiBucketVersioning(str, Enum):
    ENABLED = "Enabled"
    SUSPENDED = "Suspended"
    DISABLED = ""

    def __str__(self) -> str:
        return str(self.value)
