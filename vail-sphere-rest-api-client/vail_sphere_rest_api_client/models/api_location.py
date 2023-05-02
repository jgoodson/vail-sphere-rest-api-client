from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_location_status import ApiLocationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLocation")


@attr.s(auto_attribs=True)
class ApiLocation:
    """
    Attributes:
        name (str): Location name
        id (Union[Unset, str]): Location identifier
        latitude (Union[Unset, float]): Location latitude
        longitude (Union[Unset, float]): Location longitude
        status (Union[Unset, ApiLocationStatus]): Status
    """

    name: str
    id: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    status: Union[Unset, ApiLocationStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        latitude = self.latitude
        longitude = self.longitude
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiLocationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiLocationStatus(_status)

        api_location = cls(
            name=name,
            id=id,
            latitude=latitude,
            longitude=longitude,
            status=status,
        )

        api_location.additional_properties = d
        return api_location

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
