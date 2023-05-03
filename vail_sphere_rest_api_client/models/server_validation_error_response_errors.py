from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.server_request_error import ServerRequestError


T = TypeVar("T", bound="ServerValidationErrorResponseErrors")


@attr.s(auto_attribs=True)
class ServerValidationErrorResponseErrors:
    """a map of attributes and the errors associated with each"""

    additional_properties: Dict[str, List["ServerRequestError"]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()

                field_dict[prop_name].append(additional_property_item)

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_request_error import ServerRequestError

        d = src_dict.copy()
        server_validation_error_response_errors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = ServerRequestError.from_dict(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        server_validation_error_response_errors.additional_properties = additional_properties
        return server_validation_error_response_errors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List["ServerRequestError"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List["ServerRequestError"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
