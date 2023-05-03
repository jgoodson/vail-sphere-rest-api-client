from enum import Enum


class ApiStorageCloudProvider(str, Enum):
    AWS = "aws"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
