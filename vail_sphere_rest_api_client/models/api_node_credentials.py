from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_credentials import ApiKeyCredentials


T = TypeVar("T", bound="ApiNodeCredentials")


@_attrs_define
class ApiNodeCredentials:
    """
    Attributes:
        key_credentials (ApiKeyCredentials):
        nodekey (str): New node credentials access key
        nodesecret (str): New node credentials encrypted secret
        nonce (str): Nonce for node secret decryption
    """

    key_credentials: "ApiKeyCredentials"
    nodekey: str
    nodesecret: str
    nonce: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_credentials = self.key_credentials.to_dict()

        nodekey = self.nodekey

        nodesecret = self.nodesecret

        nonce = self.nonce

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "KeyCredentials": key_credentials,
                "nodekey": nodekey,
                "nodesecret": nodesecret,
                "nonce": nonce,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_key_credentials import ApiKeyCredentials

        d = src_dict.copy()
        key_credentials = ApiKeyCredentials.from_dict(d.pop("KeyCredentials"))

        nodekey = d.pop("nodekey")

        nodesecret = d.pop("nodesecret")

        nonce = d.pop("nonce")

        api_node_credentials = cls(
            key_credentials=key_credentials,
            nodekey=nodekey,
            nodesecret=nodesecret,
            nonce=nonce,
        )

        api_node_credentials.additional_properties = d
        return api_node_credentials

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
