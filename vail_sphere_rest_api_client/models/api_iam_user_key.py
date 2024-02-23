from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIAMUserKey")


@_attrs_define
class ApiIAMUserKey:
    """
    Attributes:
        id (str): The access key ID
        inactive (Union[Unset, bool]): Indicates the key has been disabled.
        initialized (Union[Unset, bool]): Indicates the key's secret has been provided, making it available for use.'
    """

    id: str
    inactive: Union[Unset, bool] = UNSET
    initialized: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        inactive = self.inactive

        initialized = self.initialized

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        inactive = d.pop("inactive", UNSET)

        initialized = d.pop("initialized", UNSET)

        api_iam_user_key = cls(
            id=id,
            inactive=inactive,
            initialized=initialized,
        )

        api_iam_user_key.additional_properties = d
        return api_iam_user_key

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
