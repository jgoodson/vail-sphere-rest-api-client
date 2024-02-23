from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHttpProxyResponse")


@_attrs_define
class ApiHttpProxyResponse:
    """
    Attributes:
        hostname (str): Proxy server hostname
        id (str): Proxy type
        port (int): Proxy server port
        password (Union[Unset, str]): Proxy server password
        username (Union[Unset, str]): Proxy server username
    """

    hostname: str
    id: str
    port: int
    password: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        id = self.id

        port = self.port

        password = self.password

        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "id": id,
                "port": port,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hostname = d.pop("hostname")

        id = d.pop("id")

        port = d.pop("port")

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        api_http_proxy_response = cls(
            hostname=hostname,
            id=id,
            port=port,
            password=password,
            username=username,
        )

        api_http_proxy_response.additional_properties = d
        return api_http_proxy_response

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
