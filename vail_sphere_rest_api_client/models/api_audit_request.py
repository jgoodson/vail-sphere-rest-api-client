import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_audit_request_data import ApiAuditRequestData


T = TypeVar("T", bound="ApiAuditRequest")


@_attrs_define
class ApiAuditRequest:
    """
    Attributes:
        method (str):
        path (str):
        time (datetime.datetime):
        data (Union[Unset, ApiAuditRequestData]):
    """

    method: str
    path: str
    time: datetime.datetime
    data: Union[Unset, "ApiAuditRequestData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method

        path = self.path

        time = self.time.isoformat()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "path": path,
                "time": time,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_audit_request_data import ApiAuditRequestData

        d = src_dict.copy()
        method = d.pop("method")

        path = d.pop("path")

        time = isoparse(d.pop("time"))

        _data = d.pop("data", UNSET)
        data: Union[Unset, ApiAuditRequestData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ApiAuditRequestData.from_dict(_data)

        api_audit_request = cls(
            method=method,
            path=path,
            time=time,
            data=data,
        )

        api_audit_request.additional_properties = d
        return api_audit_request

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
