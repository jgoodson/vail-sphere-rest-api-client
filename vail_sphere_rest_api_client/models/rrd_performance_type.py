from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RrdPerformanceType")


@_attrs_define
class RrdPerformanceType:
    """
    Attributes:
        description (str): Performance table description
        tables (List[str]): List of available table names
        title (str): Descriptive title
        type (str): Performance table type
    """

    description: str
    tables: List[str]
    title: str
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        tables = self.tables

        title = self.title

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "tables": tables,
                "title": title,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        tables = cast(List[str], d.pop("tables"))

        title = d.pop("title")

        type = d.pop("type")

        rrd_performance_type = cls(
            description=description,
            tables=tables,
            title=title,
            type=type,
        )

        rrd_performance_type.additional_properties = d
        return rrd_performance_type

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
