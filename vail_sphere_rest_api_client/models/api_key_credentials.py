import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ApiKeyCredentials")


@attr.s(auto_attribs=True)
class ApiKeyCredentials:
    """
    Attributes:
        expiration (datetime.datetime): When temporary credential expires
        key (str): Temporary access key
        secret (str): Temporary secret
        token (str): Temporary token
    """

    expiration: datetime.datetime
    key: str
    secret: str
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expiration = self.expiration.isoformat()

        key = self.key
        secret = self.secret
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiration": expiration,
                "key": key,
                "secret": secret,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expiration = isoparse(d.pop("expiration"))

        key = d.pop("key")

        secret = d.pop("secret")

        token = d.pop("token")

        api_key_credentials = cls(
            expiration=expiration,
            key=key,
            secret=secret,
            token=token,
        )

        api_key_credentials.additional_properties = d
        return api_key_credentials

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
