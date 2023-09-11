from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_storage_entity import ApiStorageEntity


T = TypeVar("T", bound="ApiStorageUsed")


@attr.s(auto_attribs=True)
class ApiStorageUsed:
    """
    Attributes:
        storage (List['ApiStorageEntity']): Space used by each storage that shares this physical media
        data (Union[Unset, int]): Number of bytes of object data stored
        endpoint (Union[Unset, str]): Endpoint that hosts this storage
        entity (Union[Unset, str]): Identifier for underlying physical media
        label (Union[Unset, str]): Label for bundled capacity information
        location (Union[Unset, str]): ID of location
        partial (Union[Unset, bool]): Indicates summary information is incomplete
        total (Union[Unset, int]): Maximum capacity (if storage has one)
        used (Union[Unset, int]): Number of bytes of physical media used (including overhead)
    """

    storage: List["ApiStorageEntity"]
    data: Union[Unset, int] = UNSET
    endpoint: Union[Unset, str] = UNSET
    entity: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    partial: Union[Unset, bool] = UNSET
    total: Union[Unset, int] = UNSET
    used: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage = []
        for storage_item_data in self.storage:
            storage_item = storage_item_data.to_dict()

            storage.append(storage_item)

        data = self.data
        endpoint = self.endpoint
        entity = self.entity
        label = self.label
        location = self.location
        partial = self.partial
        total = self.total
        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage": storage,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if entity is not UNSET:
            field_dict["entity"] = entity
        if label is not UNSET:
            field_dict["label"] = label
        if location is not UNSET:
            field_dict["location"] = location
        if partial is not UNSET:
            field_dict["partial"] = partial
        if total is not UNSET:
            field_dict["total"] = total
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_storage_entity import ApiStorageEntity

        d = src_dict.copy()
        storage = []
        _storage = d.pop("storage")
        for storage_item_data in _storage:
            storage_item = ApiStorageEntity.from_dict(storage_item_data)

            storage.append(storage_item)

        data = d.pop("data", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        entity = d.pop("entity", UNSET)

        label = d.pop("label", UNSET)

        location = d.pop("location", UNSET)

        partial = d.pop("partial", UNSET)

        total = d.pop("total", UNSET)

        used = d.pop("used", UNSET)

        api_storage_used = cls(
            storage=storage,
            data=data,
            endpoint=endpoint,
            entity=entity,
            label=label,
            location=location,
            partial=partial,
            total=total,
            used=used,
        )

        api_storage_used.additional_properties = d
        return api_storage_used

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
