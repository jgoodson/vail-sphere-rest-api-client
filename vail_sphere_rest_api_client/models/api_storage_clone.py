from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageClone")


@_attrs_define
class ApiStorageClone:
    """
    Attributes:
        id (str): Storage identifier
        archived (Union[Unset, bool]): Clone may require restore before access
        optional (Union[Unset, bool]): Clone will be deleted if space is needed
        partial (Union[Unset, bool]): Clone is not complete
        restored (Union[Unset, bool]): Clone is currently restored
    """

    id: str
    archived: Union[Unset, bool] = UNSET
    optional: Union[Unset, bool] = UNSET
    partial: Union[Unset, bool] = UNSET
    restored: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        archived = self.archived

        optional = self.optional

        partial = self.partial

        restored = self.restored

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if archived is not UNSET:
            field_dict["archived"] = archived
        if optional is not UNSET:
            field_dict["optional"] = optional
        if partial is not UNSET:
            field_dict["partial"] = partial
        if restored is not UNSET:
            field_dict["restored"] = restored

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        archived = d.pop("archived", UNSET)

        optional = d.pop("optional", UNSET)

        partial = d.pop("partial", UNSET)

        restored = d.pop("restored", UNSET)

        api_storage_clone = cls(
            id=id,
            archived=archived,
            optional=optional,
            partial=partial,
            restored=restored,
        )

        api_storage_clone.additional_properties = d
        return api_storage_clone

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
