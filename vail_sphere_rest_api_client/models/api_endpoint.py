from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_endpoint_status import ApiEndpointStatus
from ..models.api_endpoint_type import ApiEndpointType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpoint")


@attr.s(auto_attribs=True)
class ApiEndpoint:
    """
    Attributes:
        id (str): Endpoint identifier
        location (str): ID of physical location
        type (ApiEndpointType): Type of system running at this endpoint
        url (str): endpoint S3 URL
        debug (Union[Unset, int]): debug level (0-9)
        hosts (Union[Unset, List[str]]): additional supported hostnames
        management_url (Union[Unset, str]): URL for DS3 system management (if available)
        name (Union[Unset, str]): Name of endpoint (hostname is default).
        status (Union[Unset, ApiEndpointStatus]): Status
        version (Union[Unset, str]): current version
    """

    id: str
    location: str
    type: ApiEndpointType
    url: str
    debug: Union[Unset, int] = UNSET
    hosts: Union[Unset, List[str]] = UNSET
    management_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ApiEndpointStatus] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        location = self.location
        type = self.type.value

        url = self.url
        debug = self.debug
        hosts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        management_url = self.management_url
        name = self.name
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "location": location,
                "type": type,
                "url": url,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if management_url is not UNSET:
            field_dict["managementURL"] = management_url
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        location = d.pop("location")

        type = ApiEndpointType(d.pop("type"))

        url = d.pop("url")

        debug = d.pop("debug", UNSET)

        hosts = cast(List[str], d.pop("hosts", UNSET))

        management_url = d.pop("managementURL", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiEndpointStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointStatus(_status)

        version = d.pop("version", UNSET)

        api_endpoint = cls(
            id=id,
            location=location,
            type=type,
            url=url,
            debug=debug,
            hosts=hosts,
            management_url=management_url,
            name=name,
            status=status,
            version=version,
        )

        api_endpoint.additional_properties = d
        return api_endpoint

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
