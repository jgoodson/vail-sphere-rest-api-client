from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_node_credentials import ApiNodeCredentials
    from ..models.api_update_version import ApiUpdateVersion


T = TypeVar("T", bound="ApiRegistrationResponse")


@attr.s(auto_attribs=True)
class ApiRegistrationResponse:
    """
    Attributes:
        node_credentials (ApiNodeCredentials):
        creds_endpoint (str): Node credential server endpoint
        id (str): Node identifier
        namespace (str): Node namespace
        region (str): AWS region the Sphere is running under
        versions (List['ApiUpdateVersion']): Version map
    """

    node_credentials: "ApiNodeCredentials"
    creds_endpoint: str
    id: str
    namespace: str
    region: str
    versions: List["ApiUpdateVersion"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_credentials = self.node_credentials.to_dict()

        creds_endpoint = self.creds_endpoint
        id = self.id
        namespace = self.namespace
        region = self.region
        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()

            versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "NodeCredentials": node_credentials,
                "credsEndpoint": creds_endpoint,
                "id": id,
                "namespace": namespace,
                "region": region,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_node_credentials import ApiNodeCredentials
        from ..models.api_update_version import ApiUpdateVersion

        d = src_dict.copy()
        node_credentials = ApiNodeCredentials.from_dict(d.pop("NodeCredentials"))

        creds_endpoint = d.pop("credsEndpoint")

        id = d.pop("id")

        namespace = d.pop("namespace")

        region = d.pop("region")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = ApiUpdateVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        api_registration_response = cls(
            node_credentials=node_credentials,
            creds_endpoint=creds_endpoint,
            id=id,
            namespace=namespace,
            region=region,
            versions=versions,
        )

        api_registration_response.additional_properties = d
        return api_registration_response

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
