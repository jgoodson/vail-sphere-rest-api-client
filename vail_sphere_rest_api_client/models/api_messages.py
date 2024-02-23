from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_messages_max_unread_severity import ApiMessagesMaxUnreadSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_message import ApiMessage


T = TypeVar("T", bound="ApiMessages")


@_attrs_define
class ApiMessages:
    """
    Attributes:
        unread_count (str):
        data (List['ApiMessage']):
        is_truncated (Union[Unset, bool]): Returns true if list was truncated
        marker (Union[Unset, str]): The marker specified in the request
        max_keys (Union[Unset, int]): The maximum number of keys specified in the request
        max_unread_severity (Union[Unset, ApiMessagesMaxUnreadSeverity]): The maximum severity of the unread messages
        next_marker (Union[Unset, str]): The starting ID of the next page
    """

    unread_count: str
    data: List["ApiMessage"]
    is_truncated: Union[Unset, bool] = UNSET
    marker: Union[Unset, str] = UNSET
    max_keys: Union[Unset, int] = UNSET
    max_unread_severity: Union[Unset, ApiMessagesMaxUnreadSeverity] = UNSET
    next_marker: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unread_count = self.unread_count

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        is_truncated = self.is_truncated

        marker = self.marker

        max_keys = self.max_keys

        max_unread_severity: Union[Unset, str] = UNSET
        if not isinstance(self.max_unread_severity, Unset):
            max_unread_severity = self.max_unread_severity.value

        next_marker = self.next_marker

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "UnreadCount": unread_count,
                "data": data,
            }
        )
        if is_truncated is not UNSET:
            field_dict["isTruncated"] = is_truncated
        if marker is not UNSET:
            field_dict["marker"] = marker
        if max_keys is not UNSET:
            field_dict["maxKeys"] = max_keys
        if max_unread_severity is not UNSET:
            field_dict["maxUnreadSeverity"] = max_unread_severity
        if next_marker is not UNSET:
            field_dict["nextMarker"] = next_marker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_message import ApiMessage

        d = src_dict.copy()
        unread_count = d.pop("UnreadCount")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ApiMessage.from_dict(data_item_data)

            data.append(data_item)

        is_truncated = d.pop("isTruncated", UNSET)

        marker = d.pop("marker", UNSET)

        max_keys = d.pop("maxKeys", UNSET)

        _max_unread_severity = d.pop("maxUnreadSeverity", UNSET)
        max_unread_severity: Union[Unset, ApiMessagesMaxUnreadSeverity]
        if isinstance(_max_unread_severity, Unset):
            max_unread_severity = UNSET
        else:
            max_unread_severity = ApiMessagesMaxUnreadSeverity(_max_unread_severity)

        next_marker = d.pop("nextMarker", UNSET)

        api_messages = cls(
            unread_count=unread_count,
            data=data,
            is_truncated=is_truncated,
            marker=marker,
            max_keys=max_keys,
            max_unread_severity=max_unread_severity,
            next_marker=next_marker,
        )

        api_messages.additional_properties = d
        return api_messages

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
