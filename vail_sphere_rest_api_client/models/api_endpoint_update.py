from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointUpdate")


@attr.s(auto_attribs=True)
class ApiEndpointUpdate:
    """
    Attributes:
        debug (Union[Unset, int]): debug level (0-9)
        hosts (Union[Unset, List[str]]): additional supported hostnames
        location (Union[Unset, str]): ID of physical location
    """

    debug: Union[Unset, int] = UNSET
    hosts: Union[Unset, List[str]] = UNSET
    location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        debug = self.debug
        hosts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debug is not UNSET:
            field_dict["debug"] = debug
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        debug = d.pop("debug", UNSET)

        hosts = cast(List[str], d.pop("hosts", UNSET))

        location = d.pop("location", UNSET)

        api_endpoint_update = cls(
            debug=debug,
            hosts=hosts,
            location=location,
        )

        api_endpoint_update.additional_properties = d
        return api_endpoint_update

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
