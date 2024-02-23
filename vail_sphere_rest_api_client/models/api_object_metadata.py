from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_clone_state import ApiCloneState


T = TypeVar("T", bound="ApiObjectMetadata")


@_attrs_define
class ApiObjectMetadata:
    """
    Attributes:
        clones (ApiCloneState):
        version (str):
    """

    clones: "ApiCloneState"
    version: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clones = self.clones.to_dict()

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clones": clones,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_clone_state import ApiCloneState

        d = src_dict.copy()
        clones = ApiCloneState.from_dict(d.pop("clones"))

        version = d.pop("version")

        api_object_metadata = cls(
            clones=clones,
            version=version,
        )

        api_object_metadata.additional_properties = d
        return api_object_metadata

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
