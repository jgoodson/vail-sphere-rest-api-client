from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCloudlessSystemUpdate")


@_attrs_define
class ApiCloudlessSystemUpdate:
    """
    Attributes:
        aws_key (Union[Unset, str]): The AWS access key ID used to communicate with AWS. This is only applicable to
            cloudless configurations.
        aws_region (Union[Unset, str]): The AWS CloudFormation stack's region.
        aws_secret (Union[Unset, str]): The AWS secret access key used to communicate with AWS. This is only applicable
            to cloudless configurations.
        key (Union[Unset, str]): The sphere activation key
        monitor (Union[Unset, bool]): True if monitor events are sent to SpectraLogic.
        name (Union[Unset, str]): Name of the system
        namespace (Union[Unset, str]): The AWS CloudFormation stack's namespace.
        nightly (Union[Unset, str]): Nightly processing time (in UTC).
    """

    aws_key: Union[Unset, str] = UNSET
    aws_region: Union[Unset, str] = UNSET
    aws_secret: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    nightly: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aws_key = self.aws_key

        aws_region = self.aws_region

        aws_secret = self.aws_secret

        key = self.key

        monitor = self.monitor

        name = self.name

        namespace = self.namespace

        nightly = self.nightly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_key is not UNSET:
            field_dict["awsKey"] = aws_key
        if aws_region is not UNSET:
            field_dict["awsRegion"] = aws_region
        if aws_secret is not UNSET:
            field_dict["awsSecret"] = aws_secret
        if key is not UNSET:
            field_dict["key"] = key
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if nightly is not UNSET:
            field_dict["nightly"] = nightly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aws_key = d.pop("awsKey", UNSET)

        aws_region = d.pop("awsRegion", UNSET)

        aws_secret = d.pop("awsSecret", UNSET)

        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        nightly = d.pop("nightly", UNSET)

        api_cloudless_system_update = cls(
            aws_key=aws_key,
            aws_region=aws_region,
            aws_secret=aws_secret,
            key=key,
            monitor=monitor,
            name=name,
            namespace=namespace,
            nightly=nightly,
        )

        api_cloudless_system_update.additional_properties = d
        return api_cloudless_system_update

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
