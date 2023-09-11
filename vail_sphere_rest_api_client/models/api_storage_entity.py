from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_storage_entity_storage_class import ApiStorageEntityStorageClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageEntity")


@attr.s(auto_attribs=True)
class ApiStorageEntity:
    """
    Attributes:
        id (str): Storage ID
        storage_class (ApiStorageEntityStorageClass): Storage class
        data (Union[Unset, int]): Portion of physical media used by this storage for object data
    """

    id: str
    storage_class: ApiStorageEntityStorageClass
    data: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        storage_class = self.storage_class.value

        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "storageClass": storage_class,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        storage_class = ApiStorageEntityStorageClass(d.pop("storageClass"))

        data = d.pop("data", UNSET)

        api_storage_entity = cls(
            id=id,
            storage_class=storage_class,
            data=data,
        )

        api_storage_entity.additional_properties = d
        return api_storage_entity

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
