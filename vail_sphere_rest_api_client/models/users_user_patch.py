from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersUserPatch")


@_attrs_define
class UsersUserPatch:
    """
    Attributes:
        email (Union[Unset, str]): User's email address'
        error (Union[Unset, bool]): True if the user wants to receive Error emails
        info (Union[Unset, bool]): True if the user wants to receive Info emails
        warning (Union[Unset, bool]): True if the user wants to receive Warning emails
    """

    email: Union[Unset, str] = UNSET
    error: Union[Unset, bool] = UNSET
    info: Union[Unset, bool] = UNSET
    warning: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        error = self.error

        info = self.info

        warning = self.warning

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if error is not UNSET:
            field_dict["error"] = error
        if info is not UNSET:
            field_dict["info"] = info
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        error = d.pop("error", UNSET)

        info = d.pop("info", UNSET)

        warning = d.pop("warning", UNSET)

        users_user_patch = cls(
            email=email,
            error=error,
            info=info,
            warning=warning,
        )

        users_user_patch.additional_properties = d
        return users_user_patch

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
