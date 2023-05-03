from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystemUpdate")


@attr.s(auto_attribs=True)
class ApiSystemUpdate:
    """
    Attributes:
        key (Union[Unset, str]): The sphere activation key
        monitor (Union[Unset, bool]): True if monitor events are sent to SpectraLogic.
        name (Union[Unset, str]): Name of the system
    """

    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        monitor = self.monitor
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        name = d.pop("name", UNSET)

        api_system_update = cls(
            key=key,
            monitor=monitor,
            name=name,
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
