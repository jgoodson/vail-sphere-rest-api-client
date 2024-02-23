import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_system_common_type import ApiSystemCommonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystemCommon")


@_attrs_define
class ApiSystemCommon:
    """
    Attributes:
        name (str): Name of the system
        os (str): The system's operating system'
        type (ApiSystemCommonType): Type of system
        id (Union[Unset, str]): System identifier. Only present if the system is registered.
        key (Union[Unset, str]): The sphere activation key. Only present if the system is registered.
        monitor (Union[Unset, bool]): True if monitor events are sent to SpectraLogic.
        nightly (Union[Unset, str]): Nightly processing time (in UTC).
        sequence (Union[Unset, str]): Current sequence unique ID.
        sphere (Union[Unset, str]): The sphere credentials endpoint. Only present if the system is activated.
        time (Union[Unset, datetime.datetime]): Current system time.
    """

    name: str
    os: str
    type: ApiSystemCommonType
    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    nightly: Union[Unset, str] = UNSET
    sequence: Union[Unset, str] = UNSET
    sphere: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        os = self.os

        type = self.type.value

        id = self.id

        key = self.key

        monitor = self.monitor

        nightly = self.nightly

        sequence = self.sequence

        sphere = self.sphere

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

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
        if nightly is not UNSET:
            field_dict["nightly"] = nightly
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if sphere is not UNSET:
            field_dict["sphere"] = sphere
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        os = d.pop("os")

        type = ApiSystemCommonType(d.pop("type"))

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        nightly = d.pop("nightly", UNSET)

        sequence = d.pop("sequence", UNSET)

        sphere = d.pop("sphere", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        api_system_common = cls(
            name=name,
            os=os,
            type=type,
            id=id,
            key=key,
            monitor=monitor,
            nightly=nightly,
            sequence=sequence,
            sphere=sphere,
            time=time,
        )

        api_system_common.additional_properties = d
        return api_system_common

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
