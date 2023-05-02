from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBpPlacement")


@attr.s(auto_attribs=True)
class ApiBpPlacement:
    """
    Attributes:
        partitions (List[str]): The partitions in the bucket data policy
        id (Union[Unset, str]): Storage identifier
    """

    partitions: List[str]
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partitions = self.partitions

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partitions": partitions,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        partitions = cast(List[str], d.pop("partitions"))

        id = d.pop("id", UNSET)

        api_bp_placement = cls(
            partitions=partitions,
            id=id,
        )

        api_bp_placement.additional_properties = d
        return api_bp_placement

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
