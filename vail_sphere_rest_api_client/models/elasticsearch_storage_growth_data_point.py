import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ElasticsearchStorageGrowthDataPoint")


@attr.s(auto_attribs=True)
class ElasticsearchStorageGrowthDataPoint:
    """
    Attributes:
        x (datetime.datetime):
        y (int):
    """

    x: datetime.datetime
    y: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x = self.x.isoformat()

        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x = isoparse(d.pop("x"))

        y = d.pop("y")

        elasticsearch_storage_growth_data_point = cls(
            x=x,
            y=y,
        )

        elasticsearch_storage_growth_data_point.additional_properties = d
        return elasticsearch_storage_growth_data_point

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
