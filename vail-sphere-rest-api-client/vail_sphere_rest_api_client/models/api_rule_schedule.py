from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiRuleSchedule")


@attr.s(auto_attribs=True)
class ApiRuleSchedule:
    """
    Attributes:
        days (int): Number of days to wait before executing the rule.
    """

    days: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days = self.days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days = d.pop("days")

        api_rule_schedule = cls(
            days=days,
        )

        api_rule_schedule.additional_properties = d
        return api_rule_schedule

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
