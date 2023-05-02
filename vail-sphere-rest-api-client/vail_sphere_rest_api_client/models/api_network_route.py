from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNetworkRoute")


@attr.s(auto_attribs=True)
class ApiNetworkRoute:
    """
    Attributes:
        to (str): Destination network
        on_link (Union[Unset, bool]): Add route on link
        scope (Union[Unset, str]): Route scope
        via (Union[Unset, str]): Route to via the specified address
    """

    to: str
    on_link: Union[Unset, bool] = UNSET
    scope: Union[Unset, str] = UNSET
    via: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        to = self.to
        on_link = self.on_link
        scope = self.scope
        via = self.via

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
            }
        )
        if on_link is not UNSET:
            field_dict["onLink"] = on_link
        if scope is not UNSET:
            field_dict["scope"] = scope
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        to = d.pop("to")

        on_link = d.pop("onLink", UNSET)

        scope = d.pop("scope", UNSET)

        via = d.pop("via", UNSET)

        api_network_route = cls(
            to=to,
            on_link=on_link,
            scope=scope,
            via=via,
        )

        api_network_route.additional_properties = d
        return api_network_route

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
