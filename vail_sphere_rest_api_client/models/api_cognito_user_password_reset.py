from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiCognitoUserPasswordReset")


@_attrs_define
class ApiCognitoUserPasswordReset:
    """
    Attributes:
        confirmation_code (str): The confirmation code in the password reset email
        password (str): The new password
    """

    confirmation_code: str
    password: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confirmation_code = self.confirmation_code

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confirmationCode": confirmation_code,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        confirmation_code = d.pop("confirmationCode")

        password = d.pop("password")

        api_cognito_user_password_reset = cls(
            confirmation_code=confirmation_code,
            password=password,
        )

        api_cognito_user_password_reset.additional_properties = d
        return api_cognito_user_password_reset

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
