from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersUser")


@attr.s(auto_attribs=True)
class UsersUser:
    """
    Attributes:
        email (str): The user's email address
        id (str): The user's ID (represented as the username)
        username (str): The user's username
        error (Union[Unset, bool]): True if the user wants to receive Error emails
        info (Union[Unset, bool]): True if the user wants to receive Info emails
        warning (Union[Unset, bool]): True if the user wants to receive Warning emails
    """

    email: str
    id: str
    username: str
    error: Union[Unset, bool] = UNSET
    info: Union[Unset, bool] = UNSET
    warning: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        id = self.id
        username = self.username
        error = self.error
        info = self.info
        warning = self.warning

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "id": id,
                "username": username,
            }
        )
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
        email = d.pop("email")

        id = d.pop("id")

        username = d.pop("username")

        error = d.pop("error", UNSET)

        info = d.pop("info", UNSET)

        warning = d.pop("warning", UNSET)

        users_user = cls(
            email=email,
            id=id,
            username=username,
            error=error,
            info=info,
            warning=warning,
        )

        users_user.additional_properties = d
        return users_user

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
