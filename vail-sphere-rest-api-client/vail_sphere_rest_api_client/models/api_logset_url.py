import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ApiLogsetURL")


@attr.s(auto_attribs=True)
class ApiLogsetURL:
    """
    Attributes:
        created (datetime.datetime): When the logset was created
        key (str): The logset's name'
        url (str): URL to download the logset file.
    """

    created: datetime.datetime
    key: str
    url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created.isoformat()

        key = self.key
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "key": key,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = isoparse(d.pop("created"))

        key = d.pop("key")

        url = d.pop("url")

        api_logset_url = cls(
            created=created,
            key=key,
            url=url,
        )

        api_logset_url.additional_properties = d
        return api_logset_url

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
