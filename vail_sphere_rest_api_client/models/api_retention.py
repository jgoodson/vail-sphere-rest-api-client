from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRetention")


@attr.s(auto_attribs=True)
class ApiRetention:
    """
    Attributes:
        compliance (Union[Unset, bool]): Retention mode is set to Compliance when true, Governance when false
        days (Union[Unset, int]): Number of days to retain locked objects (days or years must be specified, not both)
        years (Union[Unset, int]): Number of years to retain locked objects (days or years must be specified, not both)
    """

    compliance: Union[Unset, bool] = UNSET
    days: Union[Unset, int] = UNSET
    years: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance = self.compliance
        days = self.days
        years = self.years

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance is not UNSET:
            field_dict["compliance"] = compliance
        if days is not UNSET:
            field_dict["days"] = days
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compliance = d.pop("compliance", UNSET)

        days = d.pop("days", UNSET)

        years = d.pop("years", UNSET)

        api_retention = cls(
            compliance=compliance,
            days=days,
            years=years,
        )

        api_retention.additional_properties = d
        return api_retention

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
