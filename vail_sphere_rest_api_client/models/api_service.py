from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_service_status import ApiServiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiService")


@_attrs_define
class ApiService:
    """
    Attributes:
        name (str): Name of the service
        delay (Union[Unset, int]): response time (in milliseconds)
        status (Union[Unset, ApiServiceStatus]): Status
    """

    name: str
    delay: Union[Unset, int] = UNSET
    status: Union[Unset, ApiServiceStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        delay = self.delay

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
        if delay is not UNSET:
            field_dict["delay"] = delay
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        delay = d.pop("delay", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiServiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiServiceStatus(_status)

        api_service = cls(
            name=name,
            delay=delay,
            status=status,
        )

        api_service.additional_properties = d
        return api_service

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
