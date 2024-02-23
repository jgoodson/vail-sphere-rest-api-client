from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystemUpdate")


@_attrs_define
class ApiSystemUpdate:
    """
    Attributes:
        key (Union[Unset, str]): The sphere activation key
        monitor (Union[Unset, bool]): True if monitor events are sent to SpectraLogic.
        name (Union[Unset, str]): Name of the system
        nightly (Union[Unset, str]): Nightly processing time (in UTC).
    """

    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    nightly: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        monitor = self.monitor

        name = self.name

        nightly = self.nightly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if name is not UNSET:
            field_dict["name"] = name
        if nightly is not UNSET:
            field_dict["nightly"] = nightly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        name = d.pop("name", UNSET)

        nightly = d.pop("nightly", UNSET)

        api_system_update = cls(
            key=key,
            monitor=monitor,
            name=name,
            nightly=nightly,
        )

        api_system_update.additional_properties = d
        return api_system_update

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
