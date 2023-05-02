from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDestinations")


@attr.s(auto_attribs=True)
class ApiDestinations:
    """
    Attributes:
        storage (List[str]): The list of destination storage.
        count (Union[Unset, int]): The number of required destinations. No count means all destinations.
    """

    storage: List[str]
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage = self.storage

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage": storage,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        storage = cast(List[str], d.pop("storage"))

        count = d.pop("count", UNSET)

        api_destinations = cls(
            storage=storage,
            count=count,
        )

        api_destinations.additional_properties = d
        return api_destinations

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
