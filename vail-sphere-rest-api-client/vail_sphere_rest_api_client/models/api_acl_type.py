from enum import Enum


class ApiACLType(str, Enum):
    CANONICALUSER = "CanonicalUser"
    GROUP = "Group"

    def __str__(self) -> str:
        return str(self.value)
