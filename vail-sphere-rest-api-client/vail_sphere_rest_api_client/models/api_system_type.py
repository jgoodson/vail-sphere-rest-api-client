from enum import Enum


class ApiSystemType(str, Enum):
    BP = "bp"
    VM = "vm"

    def __str__(self) -> str:
        return str(self.value)
