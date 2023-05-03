from enum import Enum


class ApiStorageType(str, Enum):
    AZURE = "azure"
    BP = "bp"
    FILE = "file"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
