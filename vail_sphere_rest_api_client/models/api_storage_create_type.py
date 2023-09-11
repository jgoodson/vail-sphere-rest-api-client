from enum import Enum


class ApiStorageCreateType(str, Enum):
    AZURE = "azure"
    BP = "bp"
    FILE = "file"
    GOOGLE = "google"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
