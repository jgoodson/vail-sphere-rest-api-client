import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ApiCertificate")


@_attrs_define
class ApiCertificate:
    """
    Attributes:
        issuer (str): The Issuer of the Certificate
        not_after (datetime.datetime): A timestamp of the expiration date for the certificate
        not_before (datetime.datetime): A timestamp of the start date for the certificate to be valid
        subject (str): The Subject of the Certificate
    """

    issuer: str
    not_after: datetime.datetime
    not_before: datetime.datetime
    subject: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer = self.issuer

        not_after = self.not_after.isoformat()

        not_before = self.not_before.isoformat()

        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuer": issuer,
                "notAfter": not_after,
                "notBefore": not_before,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuer = d.pop("issuer")

        not_after = isoparse(d.pop("notAfter"))

        not_before = isoparse(d.pop("notBefore"))

        subject = d.pop("subject")

        api_certificate = cls(
            issuer=issuer,
            not_after=not_after,
            not_before=not_before,
            subject=subject,
        )

        api_certificate.additional_properties = d
        return api_certificate

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
