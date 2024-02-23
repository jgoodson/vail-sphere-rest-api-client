from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMetrics")


@_attrs_define
class ApiMetrics:
    """
    Attributes:
        count (Union[Unset, int]): Number of items
        optional (Union[Unset, int]): Number of bytes of stored optional content
        size (Union[Unset, int]): Number of bytes of content
        stored (Union[Unset, int]): Number of bytes of content after compression
    """

    count: Union[Unset, int] = UNSET
    optional: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    stored: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        optional = self.optional

        size = self.size

        stored = self.stored

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if optional is not UNSET:
            field_dict["optional"] = optional
        if size is not UNSET:
            field_dict["size"] = size
        if stored is not UNSET:
            field_dict["stored"] = stored

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        optional = d.pop("optional", UNSET)

        size = d.pop("size", UNSET)

        stored = d.pop("stored", UNSET)

        api_metrics = cls(
            count=count,
            optional=optional,
            size=size,
            stored=stored,
        )

        api_metrics.additional_properties = d
        return api_metrics

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
