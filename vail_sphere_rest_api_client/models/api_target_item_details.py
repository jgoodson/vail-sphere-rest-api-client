from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_target_item_details_properties import ApiTargetItemDetailsProperties


T = TypeVar("T", bound="ApiTargetItemDetails")


@_attrs_define
class ApiTargetItemDetails:
    """
    Attributes:
        id (str): Target item ID
        target (str): Target type id
        classes (Union[Unset, List[str]]): Storage classes supported by the target item
        name (Union[Unset, str]): Name of the target item
        optional (Union[Unset, bool]): True if the target item supports optional storage
        properties (Union[Unset, ApiTargetItemDetailsProperties]): Properties specific to the target item
        threshold (Union[Unset, bool]): True if the target item supports threshold warnings
    """

    id: str
    target: str
    classes: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    optional: Union[Unset, bool] = UNSET
    properties: Union[Unset, "ApiTargetItemDetailsProperties"] = UNSET
    threshold: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        target = self.target

        classes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        name = self.name

        optional = self.optional

        properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        threshold = self.threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target": target,
            }
        )
        if classes is not UNSET:
            field_dict["classes"] = classes
        if name is not UNSET:
            field_dict["name"] = name
        if optional is not UNSET:
            field_dict["optional"] = optional
        if properties is not UNSET:
            field_dict["properties"] = properties
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_target_item_details_properties import ApiTargetItemDetailsProperties

        d = src_dict.copy()
        id = d.pop("id")

        target = d.pop("target")

        classes = cast(List[str], d.pop("classes", UNSET))

        name = d.pop("name", UNSET)

        optional = d.pop("optional", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ApiTargetItemDetailsProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ApiTargetItemDetailsProperties.from_dict(_properties)

        threshold = d.pop("threshold", UNSET)

        api_target_item_details = cls(
            id=id,
            target=target,
            classes=classes,
            name=name,
            optional=optional,
            properties=properties,
            threshold=threshold,
        )

        api_target_item_details.additional_properties = d
        return api_target_item_details

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
