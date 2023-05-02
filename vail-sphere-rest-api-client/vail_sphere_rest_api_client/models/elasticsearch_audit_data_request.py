import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.elasticsearch_audit_data_request_data import ElasticsearchAuditDataRequestData


T = TypeVar("T", bound="ElasticsearchAuditDataRequest")


@attr.s(auto_attribs=True)
class ElasticsearchAuditDataRequest:
    """
    Attributes:
        data (ElasticsearchAuditDataRequestData):
        method (str):
        path (str):
        time (datetime.datetime):
    """

    data: "ElasticsearchAuditDataRequestData"
    method: str
    path: str
    time: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        method = self.method
        path = self.path
        time = self.time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "method": method,
                "path": path,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.elasticsearch_audit_data_request_data import ElasticsearchAuditDataRequestData

        d = src_dict.copy()
        data = ElasticsearchAuditDataRequestData.from_dict(d.pop("data"))

        method = d.pop("method")

        path = d.pop("path")

        time = isoparse(d.pop("time"))

        elasticsearch_audit_data_request = cls(
            data=data,
            method=method,
            path=path,
            time=time,
        )

        elasticsearch_audit_data_request.additional_properties = d
        return elasticsearch_audit_data_request

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
