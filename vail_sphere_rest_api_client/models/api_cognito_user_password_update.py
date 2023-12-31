from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiCognitoUserPasswordUpdate")


@attr.s(auto_attribs=True)
class ApiCognitoUserPasswordUpdate:
    """
    Attributes:
        password (str): The new password
    """

    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        api_cognito_user_password_update = cls(
            password=password,
        )

        api_cognito_user_password_update.additional_properties = d
        return api_cognito_user_password_update

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
