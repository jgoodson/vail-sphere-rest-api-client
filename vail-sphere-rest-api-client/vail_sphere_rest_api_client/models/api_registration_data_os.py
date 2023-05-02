from enum import Enum


class ApiRegistrationDataOs(str, Enum):
    BP = "bp"
    UBUNTU = "ubuntu"
    VAIL = "vail"

    def __str__(self) -> str:
        return str(self.value)
