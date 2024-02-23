from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageVerification")


@_attrs_define
class ApiStorageVerification:
    """
    Attributes:
        alert (Union[Unset, bool]): Send alert messages when permanent read errors are encountered
        full (Union[Unset, bool]): Perform a full verification of readable clones
    """

    alert: Union[Unset, bool] = UNSET
    full: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert = self.alert

        full = self.full

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert is not UNSET:
            field_dict["alert"] = alert
        if full is not UNSET:
            field_dict["full"] = full

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert = d.pop("alert", UNSET)

        full = d.pop("full", UNSET)

        api_storage_verification = cls(
            alert=alert,
            full=full,
        )

        api_storage_verification.additional_properties = d
        return api_storage_verification

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
