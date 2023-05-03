from enum import Enum


class ApiRuleApply(str, Enum):
    ALL = "all"
    CURRENT = "current"
    NONCURRENT = "nonCurrent"

    def __str__(self) -> str:
        return str(self.value)
