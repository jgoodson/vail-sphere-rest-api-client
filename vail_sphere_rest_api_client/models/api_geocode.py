from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiGeocode")


@_attrs_define
class ApiGeocode:
    """
    Attributes:
        display_name (str): Display name of place (intended for search results)
        id (int): Place identifier
        latitude (float): Latitude of place
        longitude (float): Longitude of place
        name (str): Name of place
    """

    display_name: str
    id: int
    latitude: float
    longitude: float
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        id = self.id

        latitude = self.latitude

        longitude = self.longitude

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "id": id,
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName")

        id = d.pop("id")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        name = d.pop("name")

        api_geocode = cls(
            display_name=display_name,
            id=id,
            latitude=latitude,
            longitude=longitude,
            name=name,
        )

        api_geocode.additional_properties = d
        return api_geocode

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
