import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_message_severity import ApiMessageSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_message_params import ApiMessageParams


T = TypeVar("T", bound="ApiMessage")


@_attrs_define
class ApiMessage:
    """
    Attributes:
        severity (ApiMessageSeverity): The severity of the message
        text (str): The translated messages
        id (Union[Unset, str]): Message identifier
        key (Union[Unset, str]): The untranslated message key
        params (Union[Unset, ApiMessageParams]): The message parameters
        read (Union[Unset, bool]): If the message has been read
        time (Union[Unset, datetime.datetime]): The time of the message
    """

    severity: ApiMessageSeverity
    text: str
    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    params: Union[Unset, "ApiMessageParams"] = UNSET
    read: Union[Unset, bool] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severity = self.severity.value

        text = self.text

        id = self.id

        key = self.key

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        read = self.read

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "text": text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if params is not UNSET:
            field_dict["params"] = params
        if read is not UNSET:
            field_dict["read"] = read
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_message_params import ApiMessageParams

        d = src_dict.copy()
        severity = ApiMessageSeverity(d.pop("severity"))

        text = d.pop("text")

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ApiMessageParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ApiMessageParams.from_dict(_params)

        read = d.pop("read", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        api_message = cls(
            severity=severity,
            text=text,
            id=id,
            key=key,
            params=params,
            read=read,
            time=time,
        )

        api_message.additional_properties = d
        return api_message

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
