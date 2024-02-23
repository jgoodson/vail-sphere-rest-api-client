from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerUpdateStatus")


@_attrs_define
class WorkerUpdateStatus:
    """
    Attributes:
        update (str):
        detail (Union[Unset, str]):
        value (Union[Unset, int]):
    """

    update: str
    detail: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update = self.update

        detail = self.detail

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "update": update,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        update = d.pop("update")

        detail = d.pop("detail", UNSET)

        value = d.pop("value", UNSET)

        worker_update_status = cls(
            update=update,
            detail=detail,
            value=value,
        )

        worker_update_status.additional_properties = d
        return worker_update_status

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
