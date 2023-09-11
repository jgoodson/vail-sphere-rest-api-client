from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_audit_request import ApiAuditRequest
    from ..models.api_audit_resource import ApiAuditResource


T = TypeVar("T", bound="ApiAudit")


@attr.s(auto_attribs=True)
class ApiAudit:
    """
    Attributes:
        client_ip (str):
        host_ip (str):
        message (str):
        node_id (str):
        request (ApiAuditRequest):
        resource (ApiAuditResource):
        server (str):
        username (str):
        id (Union[Unset, str]): Audit identifier
    """

    client_ip: str
    host_ip: str
    message: str
    node_id: str
    request: "ApiAuditRequest"
    resource: "ApiAuditResource"
    server: str
    username: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_ip = self.client_ip
        host_ip = self.host_ip
        message = self.message
        node_id = self.node_id
        request = self.request.to_dict()

        resource = self.resource.to_dict()

        server = self.server
        username = self.username
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientIP": client_ip,
                "hostIP": host_ip,
                "message": message,
                "nodeID": node_id,
                "request": request,
                "resource": resource,
                "server": server,
                "username": username,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_audit_request import ApiAuditRequest
        from ..models.api_audit_resource import ApiAuditResource

        d = src_dict.copy()
        client_ip = d.pop("clientIP")

        host_ip = d.pop("hostIP")

        message = d.pop("message")

        node_id = d.pop("nodeID")

        request = ApiAuditRequest.from_dict(d.pop("request"))

        resource = ApiAuditResource.from_dict(d.pop("resource"))

        server = d.pop("server")

        username = d.pop("username")

        id = d.pop("id", UNSET)

        api_audit = cls(
            client_ip=client_ip,
            host_ip=host_ip,
            message=message,
            node_id=node_id,
            request=request,
            resource=resource,
            server=server,
            username=username,
            id=id,
        )

        api_audit.additional_properties = d
        return api_audit

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
