from enum import Enum


class ApiRegistrationDataType(str, Enum):
    BP = "bp"
    VM = "vm"

    def __str__(self) -> str:
        return str(self.value)
