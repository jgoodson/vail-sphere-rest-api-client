from enum import Enum


class ApiSummaryLoggingProcessStatus(str, Enum):
    DEGRADED = "degraded"
    OK = "ok"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
