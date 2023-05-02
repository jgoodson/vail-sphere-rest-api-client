from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.elasticsearch_audit_data import ElasticsearchAuditData


T = TypeVar("T", bound="HandlersAuditDataPagination")


@attr.s(auto_attribs=True)
class HandlersAuditDataPagination:
    """
    Attributes:
        data (List['ElasticsearchAuditData']):
        is_truncated (Union[Unset, bool]): Returns true if list was truncated
        marker (Union[Unset, str]): The marker specified in the request
        max_keys (Union[Unset, int]): The maximum number of keys specified in the request
        next_marker (Union[Unset, str]): The starting ID of the next page
    """

    data: List["ElasticsearchAuditData"]
    is_truncated: Union[Unset, bool] = UNSET
    marker: Union[Unset, str] = UNSET
    max_keys: Union[Unset, int] = UNSET
    next_marker: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        is_truncated = self.is_truncated
        marker = self.marker
        max_keys = self.max_keys
        next_marker = self.next_marker

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if is_truncated is not UNSET:
            field_dict["isTruncated"] = is_truncated
        if marker is not UNSET:
            field_dict["marker"] = marker
        if max_keys is not UNSET:
            field_dict["maxKeys"] = max_keys
        if next_marker is not UNSET:
            field_dict["nextMarker"] = next_marker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.elasticsearch_audit_data import ElasticsearchAuditData

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ElasticsearchAuditData.from_dict(data_item_data)

            data.append(data_item)

        is_truncated = d.pop("isTruncated", UNSET)

        marker = d.pop("marker", UNSET)

        max_keys = d.pop("maxKeys", UNSET)

        next_marker = d.pop("nextMarker", UNSET)

        handlers_audit_data_pagination = cls(
            data=data,
            is_truncated=is_truncated,
            marker=marker,
            max_keys=max_keys,
            next_marker=next_marker,
        )

        handlers_audit_data_pagination.additional_properties = d
        return handlers_audit_data_pagination

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
