from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiS3Parameters")


@_attrs_define
class ApiS3Parameters:
    """
    Attributes:
        access_key (Union[Unset, str]): The account owner's access key
        arn (Union[Unset, str]): The IAM role arn to use to access the account.  This can be used as an alternative to
            providing accessKey and secretKey
        externalid (Union[Unset, str]): The IAM role's external ID
        region (Union[Unset, str]): The region where the account resides
        secret_key (Union[Unset, str]): The account owner's secret key
    """

    access_key: Union[Unset, str] = UNSET
    arn: Union[Unset, str] = UNSET
    externalid: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key

        arn = self.arn

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

        externalid = d.pop("externalid", UNSET)

        region = d.pop("region", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        api_s3_parameters = cls(
            access_key=access_key,
            arn=arn,
            externalid=externalid,
            region=region,
            secret_key=secret_key,
        )

        api_s3_parameters.additional_properties = d
        return api_s3_parameters

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
