import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseEntitlement")


@_attrs_define
class LicenseEntitlement:
    """
    Attributes:
        dimension (str): Entitlement dimension
        value (str): Entitlement value. May be a string, float64, int32, or boolean.
        expires (Union[Unset, datetime.datetime]): Entitlement expiration date
    """

    dimension: str
    value: str
    expires: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dimension = self.dimension

        value = self.value

        expires: Union[Unset, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dimension": dimension,
                "value": value,
            }
        )
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dimension = d.pop("dimension")

        value = d.pop("value")

        _expires = d.pop("expires", UNSET)
        expires: Union[Unset, datetime.datetime]
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        license_entitlement = cls(
            dimension=dimension,
            value=value,
            expires=expires,
        )

        license_entitlement.additional_properties = d
        return license_entitlement

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
