from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_storage_cloud_provider import ApiStorageCloudProvider
from ..models.api_storage_status import ApiStorageStatus
from ..models.api_storage_storage_class import ApiStorageStorageClass
from ..models.api_storage_type import ApiStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_deprecated_bucket_owner import ApiDeprecatedBucketOwner


T = TypeVar("T", bound="ApiStorage")


@_attrs_define
class ApiStorage:
    """
    Attributes:
        endpoint (str): The id of the Vail endpoint owning this storage
        id (str): Storage identifier
        item (str): The endpoint's target item for this storage
        name (str): Storage name
        target (str): The target type for this storage
        alternate (Union[Unset, str]): ID of alternate storage to move clones to during delete
        archival (Union[Unset, bool]): Restore may be required to access data
        bucket (Union[Unset, str]): Deprecated: see target item
        bucket_owner (Union[Unset, ApiDeprecatedBucketOwner]):
        caution_threshold (Union[Unset, int]): Caution threshold capacity for the storage
        clone_restore (Union[Unset, bool]): Create a new clone when restoring this storage
        cloud_provider (Union[Unset, ApiStorageCloudProvider]): Deprecated: see target
        empty (Union[Unset, bool]): Storage has no clone data
        link (Union[Unset, str]): The vail bucket to ingest objects to
        oldest (Union[Unset, str]): The Vail version used to write the first data to the pool
        optional_data (Union[Unset, int]): Percentage of space available for optional data
        pause_notifications (Union[Unset, bool]): Link notifications are paused if true
        read_only (Union[Unset, bool]): Storage cannot be modified
        recoverable (Union[Unset, bool]): Additional content is stored to allow third-party recovery
        region (Union[Unset, str]): Deprecated: see target item properties
        status (Union[Unset, ApiStorageStatus]): Status
        storage_class (Union[Unset, ApiStorageStorageClass]): Storage class
        type (Union[Unset, ApiStorageType]): Deprecated: see target
        url (Union[Unset, str]): Deprecated: see target item properties
        verification_running (Union[Unset, bool]): Storage verification in progress
        warning_threshold (Union[Unset, int]): Warning threshold capacity for the storage
    """

    endpoint: str
    id: str
    item: str
    name: str
    target: str
    alternate: Union[Unset, str] = UNSET
    archival: Union[Unset, bool] = UNSET
    bucket: Union[Unset, str] = UNSET
    bucket_owner: Union[Unset, "ApiDeprecatedBucketOwner"] = UNSET
    caution_threshold: Union[Unset, int] = UNSET
    clone_restore: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, ApiStorageCloudProvider] = UNSET
    empty: Union[Unset, bool] = UNSET
    link: Union[Unset, str] = UNSET
    oldest: Union[Unset, str] = UNSET
    optional_data: Union[Unset, int] = UNSET
    pause_notifications: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    recoverable: Union[Unset, bool] = UNSET
    region: Union[Unset, str] = UNSET
    status: Union[Unset, ApiStorageStatus] = UNSET
    storage_class: Union[Unset, ApiStorageStorageClass] = UNSET
    type: Union[Unset, ApiStorageType] = UNSET
    url: Union[Unset, str] = UNSET
    verification_running: Union[Unset, bool] = UNSET
    warning_threshold: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint

        id = self.id

        item = self.item

        name = self.name

        target = self.target

        alternate = self.alternate

        archival = self.archival

        bucket = self.bucket

        bucket_owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bucket_owner, Unset):
            bucket_owner = self.bucket_owner.to_dict()

        caution_threshold = self.caution_threshold

        clone_restore = self.clone_restore

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider.value

        empty = self.empty

        link = self.link

        oldest = self.oldest

        optional_data = self.optional_data

        pause_notifications = self.pause_notifications

        read_only = self.read_only

        recoverable = self.recoverable

        region = self.region

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        verification_running = self.verification_running

        warning_threshold = self.warning_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "id": id,
                "item": item,
                "name": name,
                "target": target,
            }
        )
        if alternate is not UNSET:
            field_dict["alternate"] = alternate
        if archival is not UNSET:
            field_dict["archival"] = archival
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if bucket_owner is not UNSET:
            field_dict["bucketOwner"] = bucket_owner
        if caution_threshold is not UNSET:
            field_dict["cautionThreshold"] = caution_threshold
        if clone_restore is not UNSET:
            field_dict["cloneRestore"] = clone_restore
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if empty is not UNSET:
            field_dict["empty"] = empty
        if link is not UNSET:
            field_dict["link"] = link
        if oldest is not UNSET:
            field_dict["oldest"] = oldest
        if optional_data is not UNSET:
            field_dict["optionalData"] = optional_data
        if pause_notifications is not UNSET:
            field_dict["pauseNotifications"] = pause_notifications
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if recoverable is not UNSET:
            field_dict["recoverable"] = recoverable
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if verification_running is not UNSET:
            field_dict["verificationRunning"] = verification_running
        if warning_threshold is not UNSET:
            field_dict["warningThreshold"] = warning_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_deprecated_bucket_owner import ApiDeprecatedBucketOwner

        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        id = d.pop("id")

        item = d.pop("item")

        name = d.pop("name")

        target = d.pop("target")

        alternate = d.pop("alternate", UNSET)

        archival = d.pop("archival", UNSET)

        bucket = d.pop("bucket", UNSET)

        _bucket_owner = d.pop("bucketOwner", UNSET)
        bucket_owner: Union[Unset, ApiDeprecatedBucketOwner]
        if isinstance(_bucket_owner, Unset):
            bucket_owner = UNSET
        else:
            bucket_owner = ApiDeprecatedBucketOwner.from_dict(_bucket_owner)

        caution_threshold = d.pop("cautionThreshold", UNSET)

        clone_restore = d.pop("cloneRestore", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, ApiStorageCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = ApiStorageCloudProvider(_cloud_provider)

        empty = d.pop("empty", UNSET)

        link = d.pop("link", UNSET)

        oldest = d.pop("oldest", UNSET)

        optional_data = d.pop("optionalData", UNSET)

        pause_notifications = d.pop("pauseNotifications", UNSET)

        read_only = d.pop("readOnly", UNSET)

        recoverable = d.pop("recoverable", UNSET)

        region = d.pop("region", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiStorageStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiStorageStatus(_status)

        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, ApiStorageStorageClass]
        if isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = ApiStorageStorageClass(_storage_class)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ApiStorageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiStorageType(_type)

        url = d.pop("url", UNSET)

        verification_running = d.pop("verificationRunning", UNSET)

        warning_threshold = d.pop("warningThreshold", UNSET)

        api_storage = cls(
            endpoint=endpoint,
            id=id,
            item=item,
            name=name,
            target=target,
            alternate=alternate,
            archival=archival,
            bucket=bucket,
            bucket_owner=bucket_owner,
            caution_threshold=caution_threshold,
            clone_restore=clone_restore,
            cloud_provider=cloud_provider,
            empty=empty,
            link=link,
            oldest=oldest,
            optional_data=optional_data,
            pause_notifications=pause_notifications,
            read_only=read_only,
            recoverable=recoverable,
            region=region,
            status=status,
            storage_class=storage_class,
            type=type,
            url=url,
            verification_running=verification_running,
            warning_threshold=warning_threshold,
        )

        api_storage.additional_properties = d
        return api_storage

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
