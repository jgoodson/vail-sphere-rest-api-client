from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_system import ApiSystem
    from ..models.rest_token import RestToken


T = TypeVar("T", bound="HandlersNodeRegistrationInfo")


@attr.s(auto_attribs=True)
class HandlersNodeRegistrationInfo:
    """
    Attributes:
        system (ApiSystem):
        token (RestToken):
    """

    system: "ApiSystem"
    token: "RestToken"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        system = self.system.to_dict()

        token = self.token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "system": system,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_system import ApiSystem
        from ..models.rest_token import RestToken

        d = src_dict.copy()
        system = ApiSystem.from_dict(d.pop("system"))

        token = RestToken.from_dict(d.pop("token"))

        handlers_node_registration_info = cls(
            system=system,
            token=token,
        )

        handlers_node_registration_info.additional_properties = d
        return handlers_node_registration_info

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
