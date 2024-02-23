from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_storage_class_required_storage_class import ApiStorageClassRequiredStorageClass

T = TypeVar("T", bound="ApiStorageClassRequired")


@_attrs_define
class ApiStorageClassRequired:
    """
    Attributes:
        storage_class (ApiStorageClassRequiredStorageClass): Storage class
    """

    storage_class: ApiStorageClassRequiredStorageClass
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage_class = self.storage_class.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storageClass": storage_class,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        storage_class = ApiStorageClassRequiredStorageClass(d.pop("storageClass"))

        api_storage_class_required = cls(
            storage_class=storage_class,
        )

        api_storage_class_required.additional_properties = d
        return api_storage_class_required

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
