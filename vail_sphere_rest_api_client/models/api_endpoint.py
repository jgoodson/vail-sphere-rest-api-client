from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_endpoint_status import ApiEndpointStatus
from ..models.api_endpoint_type import ApiEndpointType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_update_version import ApiUpdateVersion


T = TypeVar("T", bound="ApiEndpoint")


@attr.s(auto_attribs=True)
class ApiEndpoint:
    """
    Attributes:
        endpoint (str): endpoint network address
        id (str): Endpoint identifier
        location (str): ID of physical location
        type (ApiEndpointType): Type of system running at this endpoint
        current_version (Union[Unset, str]): current version
        management_endpoint (Union[Unset, str]): endpoint for system management endpoint (if available)
        name (Union[Unset, str]): Name of endpoint (hostname is default).
        preferred_version (Union[Unset, str]): preferred version
        status (Union[Unset, ApiEndpointStatus]): Status
        versions (Union[Unset, List['ApiUpdateVersion']]): map of available versions
    """

    endpoint: str
    id: str
    location: str
    type: ApiEndpointType
    current_version: Union[Unset, str] = UNSET
    management_endpoint: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preferred_version: Union[Unset, str] = UNSET
    status: Union[Unset, ApiEndpointStatus] = UNSET
    versions: Union[Unset, List["ApiUpdateVersion"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        id = self.id
        location = self.location
        type = self.type.value

        current_version = self.current_version
        management_endpoint = self.management_endpoint
        name = self.name
        preferred_version = self.preferred_version
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()

                versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "id": id,
                "location": location,
                "type": type,
            }
        )
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if management_endpoint is not UNSET:
            field_dict["managementEndpoint"] = management_endpoint
        if name is not UNSET:
            field_dict["name"] = name
        if preferred_version is not UNSET:
            field_dict["preferredVersion"] = preferred_version
        if status is not UNSET:
            field_dict["status"] = status
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_update_version import ApiUpdateVersion

        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        id = d.pop("id")

        location = d.pop("location")

        type = ApiEndpointType(d.pop("type"))

        current_version = d.pop("currentVersion", UNSET)

        management_endpoint = d.pop("managementEndpoint", UNSET)

        name = d.pop("name", UNSET)

        preferred_version = d.pop("preferredVersion", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiEndpointStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointStatus(_status)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = ApiUpdateVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        api_endpoint = cls(
            endpoint=endpoint,
            id=id,
            location=location,
            type=type,
            current_version=current_version,
            management_endpoint=management_endpoint,
            name=name,
            preferred_version=preferred_version,
            status=status,
            versions=versions,
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
