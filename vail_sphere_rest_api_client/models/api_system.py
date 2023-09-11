from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_system_type import ApiSystemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystem")


@attr.s(auto_attribs=True)
class ApiSystem:
    """
    Attributes:
        name (str): Name of the system
        os (str): The system's operating system'
        type (ApiSystemType): Type of system
        id (Union[Unset, str]): System identifier. Only present if the system is registered.
        key (Union[Unset, str]): The sphere activation key. Only present if the system is registered.
        monitor (Union[Unset, bool]): True if monitor events are sent to SpectraLogic.
        namespace (Union[Unset, str]): The sphere name. Only present if the system is activated.
        nightly (Union[Unset, str]): Nightly processing time (in UTC).
        sphere (Union[Unset, str]): The sphere credentials endpoint. Only present if the system is activated.
    """

    name: str
    os: str
    type: ApiSystemType
    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    namespace: Union[Unset, str] = UNSET
    nightly: Union[Unset, str] = UNSET
    sphere: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        os = self.os
        type = self.type.value

        id = self.id
        key = self.key
        monitor = self.monitor
        namespace = self.namespace
        nightly = self.nightly
        sphere = self.sphere

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "os": os,
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if nightly is not UNSET:
            field_dict["nightly"] = nightly
        if sphere is not UNSET:
            field_dict["sphere"] = sphere

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        os = d.pop("os")

        type = ApiSystemType(d.pop("type"))

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        namespace = d.pop("namespace", UNSET)

        nightly = d.pop("nightly", UNSET)

        sphere = d.pop("sphere", UNSET)

        api_system = cls(
            name=name,
            os=os,
            type=type,
            id=id,
            key=key,
            monitor=monitor,
            namespace=namespace,
            nightly=nightly,
            sphere=sphere,
        )

        api_system.additional_properties = d
        return api_system

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
