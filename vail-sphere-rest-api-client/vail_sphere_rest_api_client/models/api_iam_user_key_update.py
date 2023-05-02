from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIAMUserKeyUpdate")


@attr.s(auto_attribs=True)
class ApiIAMUserKeyUpdate:
    """
    Attributes:
        inactive (Union[Unset, bool]): True if the key is to be disabled.
        secret_access_key (Union[Unset, str]): The current value of the secret access key on AWS.
    """

    inactive: Union[Unset, bool] = UNSET
    secret_access_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inactive = self.inactive
        secret_access_key = self.secret_access_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if secret_access_key is not UNSET:
            field_dict["secretAccessKey"] = secret_access_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inactive = d.pop("inactive", UNSET)

        secret_access_key = d.pop("secretAccessKey", UNSET)

        api_iam_user_key_update = cls(
            inactive=inactive,
            secret_access_key=secret_access_key,
        )

        api_iam_user_key_update.additional_properties = d
        return api_iam_user_key_update

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
