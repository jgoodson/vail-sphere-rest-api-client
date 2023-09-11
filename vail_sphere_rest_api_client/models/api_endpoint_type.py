from enum import Enum


class ApiEndpointType(str, Enum):
    BP = "bp"
    SPHERE = "sphere"
    VM = "vm"

    def __str__(self) -> str:
        return str(self.value)
