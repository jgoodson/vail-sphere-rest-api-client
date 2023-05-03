import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_storage_clone import ApiStorageClone


T = TypeVar("T", bound="ApiCloneState")


@attr.s(auto_attribs=True)
class ApiCloneState:
    """
    Attributes:
        processing (Union[Unset, bool]): Lifecycle processing is active
        restoring (Union[Unset, bool]): A restore request is active
        scheduled (Union[Unset, datetime.datetime]): Scheduled copy time
        storage (Union[Unset, List['ApiStorageClone']]): Storage clones
    """

    processing: Union[Unset, bool] = UNSET
    restoring: Union[Unset, bool] = UNSET
    scheduled: Union[Unset, datetime.datetime] = UNSET
    storage: Union[Unset, List["ApiStorageClone"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        processing = self.processing
        restoring = self.restoring
        scheduled: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled, Unset):
            scheduled = self.scheduled.isoformat()

        storage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.storage, Unset):
            storage = []
            for storage_item_data in self.storage:
                storage_item = storage_item_data.to_dict()

                storage.append(storage_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processing is not UNSET:
            field_dict["processing"] = processing
        if restoring is not UNSET:
            field_dict["restoring"] = restoring
        if scheduled is not UNSET:
            field_dict["scheduled"] = scheduled
        if storage is not UNSET:
            field_dict["storage"] = storage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_storage_clone import ApiStorageClone

        d = src_dict.copy()
        processing = d.pop("processing", UNSET)

        restoring = d.pop("restoring", UNSET)

        _scheduled = d.pop("scheduled", UNSET)
        scheduled: Union[Unset, datetime.datetime]
        if isinstance(_scheduled, Unset):
            scheduled = UNSET
        else:
            scheduled = isoparse(_scheduled)

        storage = []
        _storage = d.pop("storage", UNSET)
        for storage_item_data in _storage or []:
            storage_item = ApiStorageClone.from_dict(storage_item_data)

            storage.append(storage_item)

        api_clone_state = cls(
            processing=processing,
            restoring=restoring,
            scheduled=scheduled,
            storage=storage,
        )

        api_clone_state.additional_properties = d
        return api_clone_state

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
