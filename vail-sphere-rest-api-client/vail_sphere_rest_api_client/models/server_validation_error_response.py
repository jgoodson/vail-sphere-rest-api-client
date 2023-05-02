from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_validation_error_response_errors import ServerValidationErrorResponseErrors


T = TypeVar("T", bound="ServerValidationErrorResponse")


@attr.s(auto_attribs=True)
class ServerValidationErrorResponse:
    """
    Attributes:
        code (str): a string identifying the type of error
        message (str): a textual description of the error
        errors (Union[Unset, ServerValidationErrorResponseErrors]): a map of attributes and the errors associated with
            each
    """

    code: str
    message: str
    errors: Union[Unset, "ServerValidationErrorResponseErrors"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message
        errors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_validation_error_response_errors import ServerValidationErrorResponseErrors

        d = src_dict.copy()
        code = d.pop("code")

        message = d.pop("message")

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, ServerValidationErrorResponseErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ServerValidationErrorResponseErrors.from_dict(_errors)

        server_validation_error_response = cls(
            code=code,
            message=message,
            errors=errors,
        )

        server_validation_error_response.additional_properties = d
        return server_validation_error_response

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
