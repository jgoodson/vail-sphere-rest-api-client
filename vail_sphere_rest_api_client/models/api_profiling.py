from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProfiling")


@_attrs_define
class ApiProfiling:
    """
    Attributes:
        cpu (Union[Unset, int]): CPU profiling frequency (in seconds)
        memory (Union[Unset, int]): Memory profiling frequency (in seconds)
    """

    cpu: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu = self.cpu

        memory = self.memory

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu = d.pop("cpu", UNSET)

        memory = d.pop("memory", UNSET)

        api_profiling = cls(
            cpu=cpu,
            memory=memory,
        )

        api_profiling.additional_properties = d
        return api_profiling

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
