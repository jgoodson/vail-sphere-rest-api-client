from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_storage_update_status import ApiStorageUpdateStatus
from ..models.api_storage_update_storage_class import ApiStorageUpdateStorageClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageUpdate")


@attr.s(auto_attribs=True)
class ApiStorageUpdate:
    """
    Attributes:
        access_key (Union[Unset, str]): The account owner's access key, or the Azure storage account
        alternate (Union[Unset, str]): ID of alternate storage to move clones to during delete
        arn (Union[Unset, str]): The IAM role arn to use to access the account.  This can be used as an alternative to
            providing accessKey and secretKey.
        caution_threshold (Union[Unset, int]): Caution threshold capacity for the storage
        clone_restore (Union[Unset, bool]): Create a new clone when restoring this storage
        externalid (Union[Unset, str]): The IAM role's external ID.
        name (Union[Unset, str]): Storage name
        optional_data (Union[Unset, int]): Percentage of space available for optional data
        secret_key (Union[Unset, str]): The account owner's secret key
        status (Union[Unset, ApiStorageUpdateStatus]): Status can be set to deleting to begin background deletion
        storage_class (Union[Unset, ApiStorageUpdateStorageClass]): Storage class
        warning_threshold (Union[Unset, int]): Warning threshold capacity for the storage
    """

    access_key: Union[Unset, str] = UNSET
    alternate: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    caution_threshold: Union[Unset, int] = UNSET
    clone_restore: Union[Unset, bool] = UNSET
    externalid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    optional_data: Union[Unset, int] = UNSET
    secret_key: Union[Unset, str] = UNSET
    status: Union[Unset, ApiStorageUpdateStatus] = UNSET
    storage_class: Union[Unset, ApiStorageUpdateStorageClass] = UNSET
    warning_threshold: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key
        alternate = self.alternate
        arn = self.arn
        caution_threshold = self.caution_threshold
        clone_restore = self.clone_restore
        externalid = self.externalid
        name = self.name
        optional_data = self.optional_data
        secret_key = self.secret_key
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        warning_threshold = self.warning_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if alternate is not UNSET:
            field_dict["alternate"] = alternate
        if arn is not UNSET:
            field_dict["arn"] = arn
        if caution_threshold is not UNSET:
            field_dict["cautionThreshold"] = caution_threshold
        if clone_restore is not UNSET:
            field_dict["cloneRestore"] = clone_restore
        if externalid is not UNSET:
            field_dict["externalid"] = externalid
        if name is not UNSET:
            field_dict["name"] = name
        if optional_data is not UNSET:
            field_dict["optionalData"] = optional_data
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if status is not UNSET:
            field_dict["status"] = status
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if warning_threshold is not UNSET:
            field_dict["warningThreshold"] = warning_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key = d.pop("accessKey", UNSET)

        alternate = d.pop("alternate", UNSET)

        arn = d.pop("arn", UNSET)

        caution_threshold = d.pop("cautionThreshold", UNSET)

        clone_restore = d.pop("cloneRestore", UNSET)

        externalid = d.pop("externalid", UNSET)

        name = d.pop("name", UNSET)

        optional_data = d.pop("optionalData", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiStorageUpdateStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiStorageUpdateStatus(_status)

        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, ApiStorageUpdateStorageClass]
        if isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = ApiStorageUpdateStorageClass(_storage_class)

        warning_threshold = d.pop("warningThreshold", UNSET)

        api_storage_update = cls(
            access_key=access_key,
            alternate=alternate,
            arn=arn,
            caution_threshold=caution_threshold,
            clone_restore=clone_restore,
            externalid=externalid,
            name=name,
            optional_data=optional_data,
            secret_key=secret_key,
            status=status,
            storage_class=storage_class,
            warning_threshold=warning_threshold,
        )

        api_storage_update.additional_properties = d
        return api_storage_update

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
