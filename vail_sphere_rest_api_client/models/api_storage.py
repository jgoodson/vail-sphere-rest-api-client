from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_storage_cloud_provider import ApiStorageCloudProvider
from ..models.api_storage_status import ApiStorageStatus
from ..models.api_storage_storage_class import ApiStorageStorageClass
from ..models.api_storage_type import ApiStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_bucket_owner import ApiBucketOwner


T = TypeVar("T", bound="ApiStorage")


@attr.s(auto_attribs=True)
class ApiStorage:
    """
    Attributes:
        endpoint (str): The id of the Vail endpoint owning this storage
        id (str): Storage identifier
        name (str): Storage name
        type (ApiStorageType): Storage type
        alternate (Union[Unset, str]): ID of alternate storage to move clones to during delete
        bucket (Union[Unset, str]): The external bucket to write too
        bucket_owner (Union[Unset, ApiBucketOwner]):
        caution_threshold (Union[Unset, int]): Caution threshold capacity for the storage
        clone_restore (Union[Unset, bool]): Create a new clone when restoring this storage
        cloud_provider (Union[Unset, ApiStorageCloudProvider]): Provider of cloud services (if applicable)
        empty (Union[Unset, bool]): Storage has no clone data
        link (Union[Unset, str]): The vail bucket to ingest objects to
        oldest (Union[Unset, str]): The Vail version used to write the first data to the pool
        optional_data (Union[Unset, int]): Percentage of space available for optional data
        read_only (Union[Unset, bool]): Storage cannot be modified
        region (Union[Unset, str]): Cloud region (if applicable)
        status (Union[Unset, ApiStorageStatus]): Status
        storage_class (Union[Unset, ApiStorageStorageClass]): Storage class
        url (Union[Unset, str]): S3 data path URL (if applicable)
        verification_running (Union[Unset, bool]): Storage verification in progress
        warning_threshold (Union[Unset, int]): Warning threshold capacity for the storage
    """

    endpoint: str
    id: str
    name: str
    type: ApiStorageType
    alternate: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    bucket_owner: Union[Unset, "ApiBucketOwner"] = UNSET
    caution_threshold: Union[Unset, int] = UNSET
    clone_restore: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, ApiStorageCloudProvider] = UNSET
    empty: Union[Unset, bool] = UNSET
    link: Union[Unset, str] = UNSET
    oldest: Union[Unset, str] = UNSET
    optional_data: Union[Unset, int] = UNSET
    read_only: Union[Unset, bool] = UNSET
    region: Union[Unset, str] = UNSET
    status: Union[Unset, ApiStorageStatus] = UNSET
    storage_class: Union[Unset, ApiStorageStorageClass] = UNSET
    url: Union[Unset, str] = UNSET
    verification_running: Union[Unset, bool] = UNSET
    warning_threshold: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        id = self.id
        name = self.name
        type = self.type.value

        alternate = self.alternate
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
        read_only = self.read_only
        region = self.region
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        url = self.url
        verification_running = self.verification_running
        warning_threshold = self.warning_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "id": id,
                "name": name,
                "type": type,
            }
        )
        if alternate is not UNSET:
            field_dict["alternate"] = alternate
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
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if url is not UNSET:
            field_dict["url"] = url
        if verification_running is not UNSET:
            field_dict["verificationRunning"] = verification_running
        if warning_threshold is not UNSET:
            field_dict["warningThreshold"] = warning_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_bucket_owner import ApiBucketOwner

        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        id = d.pop("id")

        name = d.pop("name")

        type = ApiStorageType(d.pop("type"))

        alternate = d.pop("alternate", UNSET)

        bucket = d.pop("bucket", UNSET)

        _bucket_owner = d.pop("bucketOwner", UNSET)
        bucket_owner: Union[Unset, ApiBucketOwner]
        if isinstance(_bucket_owner, Unset):
            bucket_owner = UNSET
        else:
            bucket_owner = ApiBucketOwner.from_dict(_bucket_owner)

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

        read_only = d.pop("readOnly", UNSET)

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

        url = d.pop("url", UNSET)

        verification_running = d.pop("verificationRunning", UNSET)

        warning_threshold = d.pop("warningThreshold", UNSET)

        api_storage = cls(
            endpoint=endpoint,
            id=id,
            name=name,
            type=type,
            alternate=alternate,
            bucket=bucket,
            bucket_owner=bucket_owner,
            caution_threshold=caution_threshold,
            clone_restore=clone_restore,
            cloud_provider=cloud_provider,
            empty=empty,
            link=link,
            oldest=oldest,
            optional_data=optional_data,
            read_only=read_only,
            region=region,
            status=status,
            storage_class=storage_class,
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
