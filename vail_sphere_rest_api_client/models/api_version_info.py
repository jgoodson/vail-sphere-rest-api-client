from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_os_version import ApiOSVersion


T = TypeVar("T", bound="ApiVersionInfo")


@attr.s(auto_attribs=True)
class ApiVersionInfo:
    """
    Attributes:
        version (str):
        os (Union[Unset, ApiOSVersion]):
        patch (Union[Unset, bool]):
        unsafe (Union[Unset, bool]):
        url (Union[Unset, str]):
    """

    version: str
    os: Union[Unset, "ApiOSVersion"] = UNSET
    patch: Union[Unset, bool] = UNSET
    unsafe: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        os: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.os, Unset):
            os = self.os.to_dict()

        patch = self.patch
        unsafe = self.unsafe
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
            }
        )
        if os is not UNSET:
            field_dict["os"] = os
        if patch is not UNSET:
            field_dict["patch"] = patch
        if unsafe is not UNSET:
            field_dict["unsafe"] = unsafe
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_os_version import ApiOSVersion

        d = src_dict.copy()
        version = d.pop("version")

        _os = d.pop("os", UNSET)
        os: Union[Unset, ApiOSVersion]
        if isinstance(_os, Unset):
            os = UNSET
        else:
            os = ApiOSVersion.from_dict(_os)

        patch = d.pop("patch", UNSET)

        unsafe = d.pop("unsafe", UNSET)

        url = d.pop("url", UNSET)

        api_version_info = cls(
            version=version,
            os=os,
            patch=patch,
            unsafe=unsafe,
            url=url,
        )

        api_version_info.additional_properties = d
        return api_version_info

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
