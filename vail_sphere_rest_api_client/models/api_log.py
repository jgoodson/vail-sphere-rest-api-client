import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ApiLog")


@_attrs_define
class ApiLog:
    """
    Attributes:
        created (datetime.datetime): When the log set was created
        creating (bool): True if the log set is in the process of being created
        id (str): The log set's ID'
        size (int): The size of the log set in bytes
        type (str): The type of log set
    """

    created: datetime.datetime
    creating: bool
    id: str
    size: int
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created.isoformat()

        creating = self.creating

        id = self.id

        size = self.size

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "creating": creating,
                "id": id,
                "size": size,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = isoparse(d.pop("created"))

        creating = d.pop("creating")

        id = d.pop("id")

        size = d.pop("size")

        type = d.pop("type")

        api_log = cls(
            created=created,
            creating=creating,
            id=id,
            size=size,
            type=type,
        )

        api_log.additional_properties = d
        return api_log

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
