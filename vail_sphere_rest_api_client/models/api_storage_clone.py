from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageClone")


@attr.s(auto_attribs=True)
class ApiStorageClone:
    """
    Attributes:
        id (str): Storage identifier
        nearline (Union[Unset, bool]): Clone may require restore before access
        optional (Union[Unset, bool]): Clone will be deleted if space is needed
        partial (Union[Unset, bool]): Clone is not complete
        restored (Union[Unset, bool]): Clone is currently restored
    """

    id: str
    nearline: Union[Unset, bool] = UNSET
    optional: Union[Unset, bool] = UNSET
    partial: Union[Unset, bool] = UNSET
    restored: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        nearline = self.nearline
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
        if nearline is not UNSET:
            field_dict["nearline"] = nearline
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

        nearline = d.pop("nearline", UNSET)

        optional = d.pop("optional", UNSET)

        partial = d.pop("partial", UNSET)

        restored = d.pop("restored", UNSET)

        api_storage_clone = cls(
            id=id,
            nearline=nearline,
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
