from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAccountUpdate")


@_attrs_define
class ApiAccountUpdate:
    """
    Attributes:
        description (Union[Unset, str]): The AWS Account's description.
        email (Union[Unset, str]): The user's email associated with the AWS Account.
        external_id (Union[Unset, str]): AWS role external ID. This can only be updated if the account has a role set.
        role_arn (Union[Unset, str]): AWS role ARN. This can only be updated if the account originally had a role set.
    """

    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    role_arn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        email = self.email

        external_id = self.external_id

        role_arn = self.role_arn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        external_id = d.pop("externalId", UNSET)

        role_arn = d.pop("roleArn", UNSET)

        api_account_update = cls(
            description=description,
            email=email,
            external_id=external_id,
            role_arn=role_arn,
        )

        api_account_update.additional_properties = d
        return api_account_update

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
