from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_network_route import ApiNetworkRoute


T = TypeVar("T", bound="ApiNetworkInterfaceUpdate")


@attr.s(auto_attribs=True)
class ApiNetworkInterfaceUpdate:
    """
    Attributes:
        addresses (Union[Unset, List[str]]): Bound Network Addresses
        auto6 (Union[Unset, bool]): IPV6 Automatic Configuration Enabled
        dhcp4 (Union[Unset, bool]): IPV4 DHCP Enabled
        dhcp_dns (Union[Unset, bool]): Use DHCP for DNS
        gateway4 (Union[Unset, str]): Configured IPV4 Gateway
        gateway6 (Union[Unset, str]): Configured IPV6 Gateway
        mtu (Union[Unset, int]): Maximum Transmission Unit
        name_servers (Union[Unset, List[str]]): List of DNS Name Servers
        routes (Union[Unset, List['ApiNetworkRoute']]): Network routes (if any)
        search_domains (Union[Unset, List[str]]): List of DNS Search Domains
    """

    addresses: Union[Unset, List[str]] = UNSET
    auto6: Union[Unset, bool] = UNSET
    dhcp4: Union[Unset, bool] = UNSET
    dhcp_dns: Union[Unset, bool] = UNSET
    gateway4: Union[Unset, str] = UNSET
    gateway6: Union[Unset, str] = UNSET
    mtu: Union[Unset, int] = UNSET
    name_servers: Union[Unset, List[str]] = UNSET
    routes: Union[Unset, List["ApiNetworkRoute"]] = UNSET
    search_domains: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        auto6 = self.auto6
        dhcp4 = self.dhcp4
        dhcp_dns = self.dhcp_dns
        gateway4 = self.gateway4
        gateway6 = self.gateway6
        mtu = self.mtu
        name_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.name_servers, Unset):
            name_servers = self.name_servers

        routes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()

                routes.append(routes_item)

        search_domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.search_domains, Unset):
            search_domains = self.search_domains

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if auto6 is not UNSET:
            field_dict["auto6"] = auto6
        if dhcp4 is not UNSET:
            field_dict["dhcp4"] = dhcp4
        if dhcp_dns is not UNSET:
            field_dict["dhcpDns"] = dhcp_dns
        if gateway4 is not UNSET:
            field_dict["gateway4"] = gateway4
        if gateway6 is not UNSET:
            field_dict["gateway6"] = gateway6
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if name_servers is not UNSET:
            field_dict["nameServers"] = name_servers
        if routes is not UNSET:
            field_dict["routes"] = routes
        if search_domains is not UNSET:
            field_dict["searchDomains"] = search_domains

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_network_route import ApiNetworkRoute

        d = src_dict.copy()
        addresses = cast(List[str], d.pop("addresses", UNSET))

        auto6 = d.pop("auto6", UNSET)

        dhcp4 = d.pop("dhcp4", UNSET)

        dhcp_dns = d.pop("dhcpDns", UNSET)

        gateway4 = d.pop("gateway4", UNSET)

        gateway6 = d.pop("gateway6", UNSET)

        mtu = d.pop("mtu", UNSET)

        name_servers = cast(List[str], d.pop("nameServers", UNSET))

        routes = []
        _routes = d.pop("routes", UNSET)
        for routes_item_data in _routes or []:
            routes_item = ApiNetworkRoute.from_dict(routes_item_data)

            routes.append(routes_item)

        search_domains = cast(List[str], d.pop("searchDomains", UNSET))

        api_network_interface_update = cls(
            addresses=addresses,
            auto6=auto6,
            dhcp4=dhcp4,
            dhcp_dns=dhcp_dns,
            gateway4=gateway4,
            gateway6=gateway6,
            mtu=mtu,
            name_servers=name_servers,
            routes=routes,
            search_domains=search_domains,
        )

        api_network_interface_update.additional_properties = d
        return api_network_interface_update

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
