from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_storage_class_field_storage_class import ApiStorageClassFieldStorageClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageClassField")


@_attrs_define
class ApiStorageClassField:
    """
    Attributes:
        storage_class (Union[Unset, ApiStorageClassFieldStorageClass]): Storage class
    """

    storage_class: Union[Unset, ApiStorageClassFieldStorageClass] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, ApiStorageClassFieldStorageClass]
        if isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = ApiStorageClassFieldStorageClass(_storage_class)

        api_storage_class_field = cls(
            storage_class=storage_class,
        )

        api_storage_class_field.additional_properties = d
        return api_storage_class_field

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
