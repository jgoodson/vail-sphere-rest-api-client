from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPaginator")


@_attrs_define
class ApiPaginator:
    """
    Attributes:
        is_truncated (Union[Unset, bool]): Returns true if list was truncated
        marker (Union[Unset, str]): The marker specified in the request
        max_keys (Union[Unset, int]): The maximum number of keys specified in the request
        next_marker (Union[Unset, str]): The starting ID of the next page
    """

    is_truncated: Union[Unset, bool] = UNSET
    marker: Union[Unset, str] = UNSET
    max_keys: Union[Unset, int] = UNSET
    next_marker: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_truncated = self.is_truncated

        marker = self.marker

        max_keys = self.max_keys

        next_marker = self.next_marker

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_truncated is not UNSET:
            field_dict["isTruncated"] = is_truncated
        if marker is not UNSET:
            field_dict["marker"] = marker
        if max_keys is not UNSET:
            field_dict["maxKeys"] = max_keys
        if next_marker is not UNSET:
            field_dict["nextMarker"] = next_marker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_truncated = d.pop("isTruncated", UNSET)

        marker = d.pop("marker", UNSET)

        max_keys = d.pop("maxKeys", UNSET)

        next_marker = d.pop("nextMarker", UNSET)

        api_paginator = cls(
            is_truncated=is_truncated,
            marker=marker,
            max_keys=max_keys,
            next_marker=next_marker,
        )

        api_paginator.additional_properties = d
        return api_paginator

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
