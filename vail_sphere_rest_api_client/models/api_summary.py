from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiSummary")


@_attrs_define
class ApiSummary:
    """
    Attributes:
        object_count (int): Total Number of Managed Objects
        total_managed (int): Bytes of Total Managed storage
    """

    object_count: int
    total_managed: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_count = self.object_count

        total_managed = self.total_managed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objectCount": object_count,
                "totalManaged": total_managed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_count = d.pop("objectCount")

        total_managed = d.pop("totalManaged")

        api_summary = cls(
            object_count=object_count,
            total_managed=total_managed,
        )

        api_summary.additional_properties = d
        return api_summary

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
