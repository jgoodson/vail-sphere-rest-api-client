from enum import Enum


class ApiBucketUpdateVersioning(str, Enum):
    ENABLED = "Enabled"
    SUSPENDED = "Suspended"
    DISABLED = ""

    def __str__(self) -> str:
        return str(self.value)
