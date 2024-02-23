import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_object_storage_class import ApiObjectStorageClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiObject")


@_attrs_define
class ApiObject:
    """
    Attributes:
        key (str): Object name
        last_modified (datetime.datetime): Object creation time
        etag (Union[Unset, str]): A unique identifier for the object content
        is_compliance (Union[Unset, bool]): Indicates this object has a compliance lock that can't be bypassed
        is_delete (Union[Unset, bool]): Indicates this is a delete marker (which has no etag, size, or owner)
        is_latest (Union[Unset, bool]): Indicates this is the current version
        legal_hold (Union[Unset, bool]): Indicates this object cannot be deleted until the legal hold is removed
        owner_id (Union[Unset, str]): Canonical ID of the account that owns the object
        owner_name (Union[Unset, str]): Name associated with the owning account
        restored_until (Union[Unset, datetime.datetime]): If present, the object has been restored and the restore
            expires at this time
        retain_until (Union[Unset, datetime.datetime]): If present, an object lock prevents deletion until this time
        size (Union[Unset, int]): Size of the object
        storage_class (Union[Unset, ApiObjectStorageClass]): Storage class
        version_id (Union[Unset, str]): Version ID (only present when querying versions)
    """

    key: str
    last_modified: datetime.datetime
    etag: Union[Unset, str] = UNSET
    is_compliance: Union[Unset, bool] = UNSET
    is_delete: Union[Unset, bool] = UNSET
    is_latest: Union[Unset, bool] = UNSET
    legal_hold: Union[Unset, bool] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    restored_until: Union[Unset, datetime.datetime] = UNSET
    retain_until: Union[Unset, datetime.datetime] = UNSET
    size: Union[Unset, int] = UNSET
    storage_class: Union[Unset, ApiObjectStorageClass] = UNSET
    version_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        last_modified = self.last_modified.isoformat()

        etag = self.etag

        is_compliance = self.is_compliance

        is_delete = self.is_delete

        is_latest = self.is_latest

        legal_hold = self.legal_hold

        owner_id = self.owner_id

        owner_name = self.owner_name

        restored_until: Union[Unset, str] = UNSET
        if not isinstance(self.restored_until, Unset):
            restored_until = self.restored_until.isoformat()

        retain_until: Union[Unset, str] = UNSET
        if not isinstance(self.retain_until, Unset):
            retain_until = self.retain_until.isoformat()

        size = self.size

        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        version_id = self.version_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "lastModified": last_modified,
            }
        )
        if etag is not UNSET:
            field_dict["etag"] = etag
        if is_compliance is not UNSET:
            field_dict["isCompliance"] = is_compliance
        if is_delete is not UNSET:
            field_dict["isDelete"] = is_delete
        if is_latest is not UNSET:
            field_dict["isLatest"] = is_latest
        if legal_hold is not UNSET:
            field_dict["legalHold"] = legal_hold
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if restored_until is not UNSET:
            field_dict["restoredUntil"] = restored_until
        if retain_until is not UNSET:
            field_dict["retainUntil"] = retain_until
        if size is not UNSET:
            field_dict["size"] = size
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        last_modified = isoparse(d.pop("lastModified"))

        etag = d.pop("etag", UNSET)

        is_compliance = d.pop("isCompliance", UNSET)

        is_delete = d.pop("isDelete", UNSET)

        is_latest = d.pop("isLatest", UNSET)

        legal_hold = d.pop("legalHold", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        _restored_until = d.pop("restoredUntil", UNSET)
        restored_until: Union[Unset, datetime.datetime]
        if isinstance(_restored_until, Unset):
            restored_until = UNSET
        else:
            restored_until = isoparse(_restored_until)

        _retain_until = d.pop("retainUntil", UNSET)
        retain_until: Union[Unset, datetime.datetime]
        if isinstance(_retain_until, Unset):
            retain_until = UNSET
        else:
            retain_until = isoparse(_retain_until)

        size = d.pop("size", UNSET)

        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, ApiObjectStorageClass]
        if isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = ApiObjectStorageClass(_storage_class)

        version_id = d.pop("versionId", UNSET)

        api_object = cls(
            key=key,
            last_modified=last_modified,
            etag=etag,
            is_compliance=is_compliance,
            is_delete=is_delete,
            is_latest=is_latest,
            legal_hold=legal_hold,
            owner_id=owner_id,
            owner_name=owner_name,
            restored_until=restored_until,
            retain_until=retain_until,
            size=size,
            storage_class=storage_class,
            version_id=version_id,
        )

        api_object.additional_properties = d
        return api_object

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
