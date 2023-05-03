from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiCapacitySummary")


@attr.s(auto_attribs=True)
class ApiCapacitySummary:
    """
    Attributes:
        allocated (int): Bytes Allocated
        total (int): Bytes Total
        type (str): Storage Type
        used (int): Bytes Used
    """

    allocated: int
    total: int
    type: str
    used: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocated = self.allocated
        total = self.total
        type = self.type
        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocated": allocated,
                "total": total,
                "type": type,
                "used": used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allocated = d.pop("allocated")

        total = d.pop("total")

        type = d.pop("type")

        used = d.pop("used")

        api_capacity_summary = cls(
            allocated=allocated,
            total=total,
            type=type,
            used=used,
        )

        api_capacity_summary.additional_properties = d
        return api_capacity_summary

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
