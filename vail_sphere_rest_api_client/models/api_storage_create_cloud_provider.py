from enum import Enum


class ApiStorageCreateCloudProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GOOGLE = "google"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
