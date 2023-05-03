from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_storage_create_cloud_provider import ApiStorageCreateCloudProvider
from ..models.api_storage_create_storage_class import ApiStorageCreateStorageClass
from ..models.api_storage_create_type import ApiStorageCreateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStorageCreate")


@attr.s(auto_attribs=True)
class ApiStorageCreate:
    """
    Attributes:
        name (str): Storage name
        type (ApiStorageCreateType): Storage type
        access_key (Union[Unset, str]): The account owner's access key
        arn (Union[Unset, str]): The IAM role arn to use to access the account.  This can be used as an alternative to
            providing accessKey and secretKey.
        bucket (Union[Unset, str]): The external bucket to write to
        caution_threshold (Union[Unset, int]): Caution threshold capacity for the storage
        cloud_provider (Union[Unset, ApiStorageCreateCloudProvider]): Provider of cloud services (if applicable)
        endpoint (Union[Unset, str]): S3 data path URL (if applicable)
        externalid (Union[Unset, str]): The IAM role's external ID.S
        link (Union[Unset, str]): The vail bucket to ingest objects to
        region (Union[Unset, str]): The region where the account resides
        secret_key (Union[Unset, str]): The account owner's secret key
        storage_class (Union[Unset, ApiStorageCreateStorageClass]): Storage class
        system (Union[Unset, str]): The id of the Vail endpoint owning this storage
        warning_threshold (Union[Unset, int]): Warning threshold capacity for the storage
    """

    name: str
    type: ApiStorageCreateType
    access_key: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    caution_threshold: Union[Unset, int] = UNSET
    cloud_provider: Union[Unset, ApiStorageCreateCloudProvider] = UNSET
    endpoint: Union[Unset, str] = UNSET
    externalid: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    storage_class: Union[Unset, ApiStorageCreateStorageClass] = UNSET
    system: Union[Unset, str] = UNSET
    warning_threshold: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        access_key = self.access_key
        arn = self.arn
        bucket = self.bucket
        caution_threshold = self.caution_threshold
        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider.value

        endpoint = self.endpoint
        externalid = self.externalid
        link = self.link
        region = self.region
        secret_key = self.secret_key
        storage_class: Union[Unset, str] = UNSET
        if not isinstance(self.storage_class, Unset):
            storage_class = self.storage_class.value

        system = self.system
        warning_threshold = self.warning_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
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
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if externalid is not UNSET:
            field_dict["externalid"] = externalid
        if link is not UNSET:
            field_dict["link"] = link
        if region is not UNSET:
            field_dict["region"] = region
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if system is not UNSET:
            field_dict["system"] = system
        if warning_threshold is not UNSET:
            field_dict["warningThreshold"] = warning_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = ApiStorageCreateType(d.pop("type"))

        access_key = d.pop("accessKey", UNSET)

        arn = d.pop("arn", UNSET)

        bucket = d.pop("bucket", UNSET)

        caution_threshold = d.pop("cautionThreshold", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, ApiStorageCreateCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = ApiStorageCreateCloudProvider(_cloud_provider)

        endpoint = d.pop("endpoint", UNSET)

        externalid = d.pop("externalid", UNSET)

        link = d.pop("link", UNSET)

        region = d.pop("region", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        _storage_class = d.pop("storageClass", UNSET)
        storage_class: Union[Unset, ApiStorageCreateStorageClass]
        if isinstance(_storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = ApiStorageCreateStorageClass(_storage_class)

        system = d.pop("system", UNSET)

        warning_threshold = d.pop("warningThreshold", UNSET)

        api_storage_create = cls(
            name=name,
            type=type,
            access_key=access_key,
            arn=arn,
            bucket=bucket,
            caution_threshold=caution_threshold,
            cloud_provider=cloud_provider,
            endpoint=endpoint,
            externalid=externalid,
            link=link,
            region=region,
            secret_key=secret_key,
            storage_class=storage_class,
            system=system,
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
