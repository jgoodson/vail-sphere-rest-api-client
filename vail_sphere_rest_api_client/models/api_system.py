import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_system_type import ApiSystemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystem")


@_attrs_define
class ApiSystem:
    """
    Attributes:
        name (str): Name of the system
        os (str): The system's operating system'
        type (ApiSystemType): Type of system
        allocation (Union[Unset, int]): Target memory usage for in-flight data (in bytes).
        aws_account_id (Union[Unset, str]): The sphere's AWS account ID. Only present if the system is activated.
        aws_region (Union[Unset, str]): The sphere's AWS region. Only present if the system is activated.
        connections (Union[Unset, int]): Maximum number of socket connections.
        id (Union[Unset, str]): System identifier. Only present if the system is registered.
        key (Union[Unset, str]): The sphere activation key. Only present if the system is registered.
        monitor (Union[Unset, bool]): True if monitor events are sent to SpectraLogic.
        namespace (Union[Unset, str]): The sphere name. Only present if the system is activated.
        nightly (Union[Unset, str]): Nightly processing time (in UTC).
        pid (Union[Unset, int]): The active process ID.
        sequence (Union[Unset, str]): Current sequence unique ID.
        sphere (Union[Unset, str]): The sphere credentials endpoint. Only present if the system is activated.
        time (Union[Unset, datetime.datetime]): Current system time.
    """

    name: str
    os: str
    type: ApiSystemType
    allocation: Union[Unset, int] = UNSET
    aws_account_id: Union[Unset, str] = UNSET
    aws_region: Union[Unset, str] = UNSET
    connections: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    namespace: Union[Unset, str] = UNSET
    nightly: Union[Unset, str] = UNSET
    pid: Union[Unset, int] = UNSET
    sequence: Union[Unset, str] = UNSET
    sphere: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        os = self.os

        type = self.type.value

        allocation = self.allocation

        aws_account_id = self.aws_account_id

        aws_region = self.aws_region

        connections = self.connections

        id = self.id

        key = self.key

        monitor = self.monitor

        namespace = self.namespace

        nightly = self.nightly

        pid = self.pid

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
        if allocation is not UNSET:
            field_dict["allocation"] = allocation
        if aws_account_id is not UNSET:
            field_dict["awsAccountId"] = aws_account_id
        if aws_region is not UNSET:
            field_dict["awsRegion"] = aws_region
        if connections is not UNSET:
            field_dict["connections"] = connections
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
        if pid is not UNSET:
            field_dict["pid"] = pid
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

        type = ApiSystemType(d.pop("type"))

        allocation = d.pop("allocation", UNSET)

        aws_account_id = d.pop("awsAccountId", UNSET)

        aws_region = d.pop("awsRegion", UNSET)

        connections = d.pop("connections", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        namespace = d.pop("namespace", UNSET)

        nightly = d.pop("nightly", UNSET)

        pid = d.pop("pid", UNSET)

        sequence = d.pop("sequence", UNSET)

        sphere = d.pop("sphere", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        api_system = cls(
            name=name,
            os=os,
            type=type,
            allocation=allocation,
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            connections=connections,
            id=id,
            key=key,
            monitor=monitor,
            namespace=namespace,
            nightly=nightly,
            pid=pid,
            sequence=sequence,
            sphere=sphere,
            time=time,
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
