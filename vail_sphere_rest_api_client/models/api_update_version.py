from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_os_version import ApiOSVersion
    from ..models.api_version_info import ApiVersionInfo


T = TypeVar("T", bound="ApiUpdateVersion")


@attr.s(auto_attribs=True)
class ApiUpdateVersion:
    """
    Attributes:
        binary (Union[Unset, ApiVersionInfo]):
        for_ (Union[Unset, List['ApiOSVersion']]):
        from_ (Union[Unset, List[str]]):
    """

    binary: Union[Unset, "ApiVersionInfo"] = UNSET
    for_: Union[Unset, List["ApiOSVersion"]] = UNSET
    from_: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        binary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.binary, Unset):
            binary = self.binary.to_dict()

        for_: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.for_, Unset):
            for_ = []
            for for_item_data in self.for_:
                for_item = for_item_data.to_dict()

                for_.append(for_item)

        from_: Union[Unset, List[str]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if binary is not UNSET:
            field_dict["binary"] = binary
        if for_ is not UNSET:
            field_dict["for"] = for_
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_os_version import ApiOSVersion
        from ..models.api_version_info import ApiVersionInfo

        d = src_dict.copy()
        _binary = d.pop("binary", UNSET)
        binary: Union[Unset, ApiVersionInfo]
        if isinstance(_binary, Unset):
            binary = UNSET
        else:
            binary = ApiVersionInfo.from_dict(_binary)

        for_ = []
        _for_ = d.pop("for", UNSET)
        for for_item_data in _for_ or []:
            for_item = ApiOSVersion.from_dict(for_item_data)

            for_.append(for_item)

        from_ = cast(List[str], d.pop("from", UNSET))

        api_update_version = cls(
            binary=binary,
            for_=for_,
            from_=from_,
        )

        api_update_version.additional_properties = d
        return api_update_version

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
