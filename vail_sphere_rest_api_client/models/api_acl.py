from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_acl_type import ApiACLType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiACL")


@_attrs_define
class ApiACL:
    """
    Attributes:
        id (str): Canonical user ID or group URI
        type (ApiACLType):
        read (Union[Unset, bool]): Grant READ permission
        read_acp (Union[Unset, bool]): Grant READ_ACP permission
        write (Union[Unset, bool]): Grant WRITE permission
        write_acp (Union[Unset, bool]): Grant WRITE_ACP permission
    """

    id: str
    type: ApiACLType
    read: Union[Unset, bool] = UNSET
    read_acp: Union[Unset, bool] = UNSET
    write: Union[Unset, bool] = UNSET
    write_acp: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        read = self.read

        read_acp = self.read_acp

        write = self.write

        write_acp = self.write_acp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if read is not UNSET:
            field_dict["read"] = read
        if read_acp is not UNSET:
            field_dict["readACP"] = read_acp
        if write is not UNSET:
            field_dict["write"] = write
        if write_acp is not UNSET:
            field_dict["writeACP"] = write_acp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = ApiACLType(d.pop("type"))

        read = d.pop("read", UNSET)

        read_acp = d.pop("readACP", UNSET)

        write = d.pop("write", UNSET)

        write_acp = d.pop("writeACP", UNSET)

        api_acl = cls(
            id=id,
            type=type,
            read=read,
            read_acp=read_acp,
            write=write,
            write_acp=write_acp,
        )

        api_acl.additional_properties = d
        return api_acl

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
