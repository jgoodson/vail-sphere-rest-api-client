from enum import Enum


class ApiMessagesMaxUnreadSeverity(str, Enum):
    ERROR = "error"
    INFO = "info"
    OK = "ok"
    UNKNOWN = "unknown"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
