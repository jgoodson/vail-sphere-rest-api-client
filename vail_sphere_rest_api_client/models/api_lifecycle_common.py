from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rule import ApiRule


T = TypeVar("T", bound="ApiLifecycleCommon")


@attr.s(auto_attribs=True)
class ApiLifecycleCommon:
    """
    Attributes:
        description (Union[Unset, str]): The lifecycle's description
        markers (Union[Unset, bool]): True if expired delete markers should be deleted
        rules (Union[Unset, List['ApiRule']]): The lifecycle's rules
        uploads (Union[Unset, int]): The number of days to wait before deleting incomplete multipart uploads
    """

    description: Union[Unset, str] = UNSET
    markers: Union[Unset, bool] = UNSET
    rules: Union[Unset, List["ApiRule"]] = UNSET
    uploads: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        markers = self.markers
        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        uploads = self.uploads

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if markers is not UNSET:
            field_dict["markers"] = markers
        if rules is not UNSET:
            field_dict["rules"] = rules
        if uploads is not UNSET:
            field_dict["uploads"] = uploads

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_rule import ApiRule

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        markers = d.pop("markers", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = ApiRule.from_dict(rules_item_data)

            rules.append(rules_item)

        uploads = d.pop("uploads", UNSET)

        api_lifecycle_common = cls(
            description=description,
            markers=markers,
            rules=rules,
            uploads=uploads,
        )

        api_lifecycle_common.additional_properties = d
        return api_lifecycle_common

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
