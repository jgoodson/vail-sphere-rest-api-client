from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_registration_data_os import ApiRegistrationDataOs
from ..models.api_registration_data_type import ApiRegistrationDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRegistrationData")


@attr.s(auto_attribs=True)
class ApiRegistrationData:
    """
    Attributes:
        location (str): ID of physical location
        type (ApiRegistrationDataType): Type of system running at this endpoint
        name (Union[Unset, str]): Name of endpoint (hostname is default).
        os (Union[Unset, ApiRegistrationDataOs]): Operating system for the endpoint Default:
            ApiRegistrationDataOs.UBUNTU.
    """

    location: str
    type: ApiRegistrationDataType
    name: Union[Unset, str] = UNSET
    os: Union[Unset, ApiRegistrationDataOs] = ApiRegistrationDataOs.UBUNTU
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location
        type = self.type.value

        name = self.name
        os: Union[Unset, str] = UNSET
        if not isinstance(self.os, Unset):
            os = self.os.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location = d.pop("location")

        type = ApiRegistrationDataType(d.pop("type"))

        name = d.pop("name", UNSET)

        _os = d.pop("os", UNSET)
        os: Union[Unset, ApiRegistrationDataOs]
        if isinstance(_os, Unset):
            os = UNSET
        else:
            os = ApiRegistrationDataOs(_os)

        api_registration_data = cls(
            location=location,
            type=type,
            name=name,
            os=os,
        )

        api_registration_data.additional_properties = d
        return api_registration_data

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
