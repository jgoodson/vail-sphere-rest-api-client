from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_s3_bucket_request_cloud_provider import ApiS3BucketRequestCloudProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiS3BucketRequest")


@attr.s(auto_attribs=True)
class ApiS3BucketRequest:
    """
    Attributes:
        access_key (Union[Unset, str]): The account owner's access key
        arn (Union[Unset, str]): The IAM role arn to use to access the account.  This can be used as an alternative to
            providing accessKey and secretKey.
        cloud_provider (Union[Unset, ApiS3BucketRequestCloudProvider]): Provider of cloud services (if applicable)
        endpoint (Union[Unset, str]): S3 data path URL (if applicable)
        externalid (Union[Unset, str]): The IAM role's external ID.S
        region (Union[Unset, str]): The region where the account resides
        secret_key (Union[Unset, str]): The account owner's secret key
    """

    access_key: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, ApiS3BucketRequestCloudProvider] = UNSET
    endpoint: Union[Unset, str] = UNSET
    externalid: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key
        arn = self.arn
        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider.value

        endpoint = self.endpoint
        externalid = self.externalid
        region = self.region
        secret_key = self.secret_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if arn is not UNSET:
            field_dict["arn"] = arn
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if externalid is not UNSET:
            field_dict["externalid"] = externalid
        if region is not UNSET:
            field_dict["region"] = region
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key = d.pop("accessKey", UNSET)

        arn = d.pop("arn", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, ApiS3BucketRequestCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = ApiS3BucketRequestCloudProvider(_cloud_provider)

        endpoint = d.pop("endpoint", UNSET)

        externalid = d.pop("externalid", UNSET)

        region = d.pop("region", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        api_s3_bucket_request = cls(
            access_key=access_key,
            arn=arn,
            cloud_provider=cloud_provider,
            endpoint=endpoint,
            externalid=externalid,
            region=region,
            secret_key=secret_key,
        )

        api_s3_bucket_request.additional_properties = d
        return api_s3_bucket_request

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
