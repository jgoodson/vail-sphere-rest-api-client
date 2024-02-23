from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoint_status_field_status import ApiEndpointStatusFieldStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointStatusField")


@_attrs_define
class ApiEndpointStatusField:
    """
    Attributes:
        status (Union[Unset, ApiEndpointStatusFieldStatus]): Status
    """

    status: Union[Unset, ApiEndpointStatusFieldStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiEndpointStatusFieldStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointStatusFieldStatus(_status)

        api_endpoint_status_field = cls(
            status=status,
        )

        api_endpoint_status_field.additional_properties = d
        return api_endpoint_status_field

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
