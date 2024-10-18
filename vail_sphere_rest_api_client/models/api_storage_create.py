from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_storage_create_cloud_provider import ApiStorageCreateCloudProvider
from ..models.api_storage_create_storage_class import ApiStorageCreateStorageClass
from ..models.api_storage_create_type import ApiStorageCreateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_storage_create_parameters import ApiStorageCreateParameters


T = TypeVar("T", bound="ApiStorageCreate")


@_attrs_define
class ApiStorageCreate:
    """
    Attributes:
        endpoint (str): The id of the Vail endpoint owning this storage
        item (str): The endpoint's target item ID for this storage
        name (str): Storage name
        target (str): The type of target for this storage
        access_key (Union[Unset, str]): Deprecated: use target parameters
        arn (Union[Unset, str]): Deprecated: use target parameters
        bucket (Union[Unset, str]): Deprecated: use target instead
        caution_threshold (Union[Unset, int]): Caution threshold capacity for the storage
        clone_restore (Union[Unset, bool]): Create a new clone when restoring this storage
        cloud_provider (Union[Unset, ApiStorageCreateCloudProvider]): Deprecated: use target parameters
        credentials (Union[Unset, str]): Deprecated: use target parameters
        externalid (Union[Unset, str]): Deprecated: use target parameters
        link (Union[Unset, str]): The vail bucket to ingest objects to
        optional_data (Union[Unset, int]): Percentage of space available for optional data
        parameters (Union[Unset, ApiStorageCreateParameters]): Target parameters specific to the target type.
        pause_notifications (Union[Unset, bool]): Link notifications are paused if true
        recoverable (Union[Unset, bool]): Additional content is stored to allow third-party recovery
        region (Union[Unset, str]): Deprecated: use target parameters
        secret_key (Union[Unset, str]): Deprecated: use target parameters
        storage_class (Union[Unset, ApiStorageCreateStorageClass]): Storage class
        type (Union[Unset, ApiStorageCreateType]): Deprecated: use target instead
        url (Union[Unset, str]): Deprecated: use target parameters
        warning_threshold (Union[Unset, int]): Warning threshold capacity for the storage
    """

    endpoint: str
    item: str
    name: str
    target: str
    access_key: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    caution_threshold: Union[Unset, int] = UNSET
    clone_restore: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, ApiStorageCreateCloudProvider] = UNSET
    credentials: Union[Unset, str] = UNSET
    externalid: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    optional_data: Union[Unset, int] = UNSET
    parameters: Union[Unset, "ApiStorageCreateParameters"] = UNSET
    pause_notifications: Union[Unset, bool] = UNSET
    recoverable: Union[Unset, bool] = UNSET
    region: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    storage_class: Union[Unset, ApiStorageCreateStorageClass] = UNSET
    type: Union[Unset, ApiStorageCreateType] = UNSET
    url: Union[Unset, str] = UNSET
    warning_threshold: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint

        item = self.item

        name = self.name

        target = self.target

        access_key = self.access_key

        arn = self.arn

        bucket = self.bucket

        caution_threshold = self.caution_threshold

        clone_restore = self.clone_restore

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider.value

        credentials = self.credentials

        externalid = self.externalid

        link = self.link

        optional_data = self.optional_data

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        pause_notifications = self.pause_notifications

        recoverable = self.recoverable

        region = self.region

        secret_key = self.secret_key

        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        warning_threshold = self.warning_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "item": item,
                "name": name,
                "target": target,
            }
        )
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if arn is not UNSET:
            field_dict["arn"] = arn
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if caution_threshold is not UNSET:
            field_dict["cautionThreshold"] = caution_threshold
        if clone_restore is not UNSET:
            field_dict["cloneRestore"] = clone_restore
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if externalid is not UNSET:
            field_dict["externalid"] = externalid
        if link is not UNSET:
            field_dict["link"] = link
        if optional_data is not UNSET:
            field_dict["optionalData"] = optional_data
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if pause_notifications is not UNSET:
            field_dict["pauseNotifications"] = pause_notifications
        if recoverable is not UNSET:
            field_dict["recoverable"] = recoverable
        if region is not UNSET:
            field_dict["region"] = region
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if warning_threshold is not UNSET:
            field_dict["warningThreshold"] = warning_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_storage_create_parameters import ApiStorageCreateParameters

        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        item = d.pop("item")

        name = d.pop("name")

        target = d.pop("target")

        access_key = d.pop("accessKey", UNSET)

        arn = d.pop("arn", UNSET)

        bucket = d.pop("bucket", UNSET)

        caution_threshold = d.pop("cautionThreshold", UNSET)

        clone_restore = d.pop("cloneRestore", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, ApiStorageCreateCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = ApiStorageCreateCloudProvider(_cloud_provider)

        credentials = d.pop("credentials", UNSET)

        externalid = d.pop("externalid", UNSET)

        link = d.pop("link", UNSET)

        optional_data = d.pop("optionalData", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ApiStorageCreateParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ApiStorageCreateParameters.from_dict(_parameters)

        pause_notifications = d.pop("pauseNotifications", UNSET)

        recoverable = d.pop("recoverable", UNSET)

        region = d.pop("region", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, ApiStorageCreateStorageClass]
        if isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = ApiStorageCreateStorageClass(_storage_class)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ApiStorageCreateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiStorageCreateType(_type)

        url = d.pop("url", UNSET)

        warning_threshold = d.pop("warningThreshold", UNSET)

        api_storage_create = cls(
            endpoint=endpoint,
            item=item,
            name=name,
            target=target,
            access_key=access_key,
            arn=arn,
            bucket=bucket,
            caution_threshold=caution_threshold,
            clone_restore=clone_restore,
            cloud_provider=cloud_provider,
            credentials=credentials,
            externalid=externalid,
            link=link,
            optional_data=optional_data,
            parameters=parameters,
            pause_notifications=pause_notifications,
            recoverable=recoverable,
            region=region,
            secret_key=secret_key,
            storage_class=storage_class,
            type=type,
            url=url,
            warning_threshold=warning_threshold,
        )

        api_storage_create.additional_properties = d
        return api_storage_create

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
