from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiCertificateUpdate")


@_attrs_define
class ApiCertificateUpdate:
    """
    Attributes:
        cert_pem (str): The Certificate PEM
        passphrase (str): The Passphrase for the Encrypted Private Key
        private_key_pem (str): The Private Key PEM
    """

    cert_pem: str
    passphrase: str
    private_key_pem: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_pem = self.cert_pem

        passphrase = self.passphrase

        private_key_pem = self.private_key_pem

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certPEM": cert_pem,
                "passphrase": passphrase,
                "privateKeyPEM": private_key_pem,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_pem = d.pop("certPEM")

        passphrase = d.pop("passphrase")

        private_key_pem = d.pop("privateKeyPEM")

        api_certificate_update = cls(
            cert_pem=cert_pem,
            passphrase=passphrase,
            private_key_pem=private_key_pem,
        )

        api_certificate_update.additional_properties = d
        return api_certificate_update

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
