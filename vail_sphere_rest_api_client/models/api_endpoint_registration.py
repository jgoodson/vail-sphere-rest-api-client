from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointRegistration")


@_attrs_define
class ApiEndpointRegistration:
    """
    Attributes:
        location (str): ID of physical location
        name (Union[Unset, str]): Name of endpoint (hostname is default).
        version (Union[Unset, str]): current version
    """

    location: str
    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location

        name = self.name

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location = d.pop("location")

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        api_endpoint_registration = cls(
            location=location,
            name=name,
            version=version,
        )

        api_endpoint_registration.additional_properties = d
        return api_endpoint_registration

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
