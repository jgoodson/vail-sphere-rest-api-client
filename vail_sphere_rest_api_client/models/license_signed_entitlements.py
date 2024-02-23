from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.license_entitlement import LicenseEntitlement


T = TypeVar("T", bound="LicenseSignedEntitlements")


@_attrs_define
class LicenseSignedEntitlements:
    """
    Attributes:
        entitlements (List['LicenseEntitlement']): Entitlements
        id (str): Machine ID
        signature (str): Signature
    """

    entitlements: List["LicenseEntitlement"]
    id: str
    signature: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entitlements = []
        for entitlements_item_data in self.entitlements:
            entitlements_item = entitlements_item_data.to_dict()
            entitlements.append(entitlements_item)

        id = self.id

        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entitlements": entitlements,
                "id": id,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.license_entitlement import LicenseEntitlement

        d = src_dict.copy()
        entitlements = []
        _entitlements = d.pop("entitlements")
        for entitlements_item_data in _entitlements:
            entitlements_item = LicenseEntitlement.from_dict(entitlements_item_data)

            entitlements.append(entitlements_item)

        id = d.pop("id")

        signature = d.pop("signature")

        license_signed_entitlements = cls(
            entitlements=entitlements,
            id=id,
            signature=signature,
        )

        license_signed_entitlements.additional_properties = d
        return license_signed_entitlements

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
