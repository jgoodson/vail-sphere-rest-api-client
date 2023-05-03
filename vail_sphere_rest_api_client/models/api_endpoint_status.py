from enum import Enum


class ApiEndpointStatus(str, Enum):
    DEGRADED = "degraded"
    OK = "ok"
    UNAVAILABLE = "unavailable"
    UPDATING = "updating"

    def __str__(self) -> str:
        return str(self.value)
