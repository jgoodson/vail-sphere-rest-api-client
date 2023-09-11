from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAccount")


@attr.s(auto_attribs=True)
class ApiAccount:
    """
    Attributes:
        canonical_id (Union[Unset, str]): AWS canonical ID
        default (Union[Unset, bool]): True if this is the default bucket owner account
        description (Union[Unset, str]): The AWS Account's description.
        email (Union[Unset, str]): The user's email associated with the AWS Account.
        external_id (Union[Unset, str]): External ID
        id (Union[Unset, str]): AWS account ID
        role_arn (Union[Unset, str]): AWS Role ARN
        username (Union[Unset, str]): The user's name associated with the AWS Account.
    """

    canonical_id: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    role_arn: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        canonical_id = self.canonical_id
        default = self.default
        description = self.description
        email = self.email
        external_id = self.external_id
        id = self.id
        role_arn = self.role_arn
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if canonical_id is not UNSET:
            field_dict["canonicalId"] = canonical_id
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if id is not UNSET:
            field_dict["id"] = id
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        canonical_id = d.pop("canonicalId", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        external_id = d.pop("externalId", UNSET)

        id = d.pop("id", UNSET)

        role_arn = d.pop("roleArn", UNSET)

        username = d.pop("username", UNSET)

        api_account = cls(
            canonical_id=canonical_id,
            default=default,
            description=description,
            email=email,
            external_id=external_id,
            id=id,
            role_arn=role_arn,
            username=username,
        )

        api_account.additional_properties = d
        return api_account

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
