from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiBlackPearlCredentials")


@attr.s(auto_attribs=True)
class ApiBlackPearlCredentials:
    """
    Attributes:
        access_key (str): BlackPearl user's S3 Access ID
        secret_key (str): BlackPearl user's S3 Secret Key
    """

    access_key: str
    secret_key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key
        secret_key = self.secret_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessKey": access_key,
                "secretKey": secret_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key = d.pop("accessKey")

        secret_key = d.pop("secretKey")

        api_black_pearl_credentials = cls(
            access_key=access_key,
            secret_key=secret_key,
        )

        api_black_pearl_credentials.additional_properties = d
        return api_black_pearl_credentials

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
