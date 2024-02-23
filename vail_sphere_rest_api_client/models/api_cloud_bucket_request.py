from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_cloud_bucket_request_cloud_provider import ApiCloudBucketRequestCloudProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCloudBucketRequest")


@_attrs_define
class ApiCloudBucketRequest:
    """
    Attributes:
        access_key (Union[Unset, str]): The account owner's access key, or the Azure storage account
        arn (Union[Unset, str]): The IAM role arn to use to access the account.  This can be used as an alternative to
            providing accessKey and secretKey.
        cloud_provider (Union[Unset, ApiCloudBucketRequestCloudProvider]): Provider of cloud services (if applicable)
        credentials (Union[Unset, str]): Credentials as a single element (e.g. Google JSON file)
        externalid (Union[Unset, str]): The IAM role's external ID.S
        region (Union[Unset, str]): The region where the account resides
        secret_key (Union[Unset, str]): The account owner's secret key
        url (Union[Unset, str]): S3 data path URL (if applicable)
    """

    access_key: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, ApiCloudBucketRequestCloudProvider] = UNSET
    credentials: Union[Unset, str] = UNSET
    externalid: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key

        arn = self.arn

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider.value

        credentials = self.credentials

        externalid = self.externalid

        region = self.region

        secret_key = self.secret_key

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if arn is not UNSET:
            field_dict["arn"] = arn
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if externalid is not UNSET:
            field_dict["externalid"] = externalid
        if region is not UNSET:
            field_dict["region"] = region
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key = d.pop("accessKey", UNSET)

        arn = d.pop("arn", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, ApiCloudBucketRequestCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = ApiCloudBucketRequestCloudProvider(_cloud_provider)

        credentials = d.pop("credentials", UNSET)

        externalid = d.pop("externalid", UNSET)

        region = d.pop("region", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        url = d.pop("url", UNSET)

        api_cloud_bucket_request = cls(
            access_key=access_key,
            arn=arn,
            cloud_provider=cloud_provider,
            credentials=credentials,
            externalid=externalid,
            region=region,
            secret_key=secret_key,
            url=url,
        )

        api_cloud_bucket_request.additional_properties = d
        return api_cloud_bucket_request

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
