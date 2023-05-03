from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAvailable")


@attr.s(auto_attribs=True)
class ApiAvailable:
    """
    Attributes:
        available_version (Union[Unset, str]): Sphere wide latest available version
        preferred_version (Union[Unset, str]): Sphere wide current preferred version
    """

    available_version: Union[Unset, str] = UNSET
    preferred_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_version = self.available_version
        preferred_version = self.preferred_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_version is not UNSET:
            field_dict["availableVersion"] = available_version
        if preferred_version is not UNSET:
            field_dict["preferredVersion"] = preferred_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available_version = d.pop("availableVersion", UNSET)

        preferred_version = d.pop("preferredVersion", UNSET)

        api_available = cls(
            available_version=available_version,
            preferred_version=preferred_version,
        )

        api_available.additional_properties = d
        return api_available

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
