from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_statement import ApiStatement


T = TypeVar("T", bound="ApiPolicy")


@_attrs_define
class ApiPolicy:
    """
    Attributes:
        statement (List['ApiStatement']):
        version (str):
        id (Union[Unset, str]):
    """

    statement: List["ApiStatement"]
    version: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statement = []
        for statement_item_data in self.statement:
            statement_item = statement_item_data.to_dict()
            statement.append(statement_item)

        version = self.version

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Statement": statement,
                "Version": version,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_statement import ApiStatement

        d = src_dict.copy()
        statement = []
        _statement = d.pop("Statement")
        for statement_item_data in _statement:
            statement_item = ApiStatement.from_dict(statement_item_data)

            statement.append(statement_item)

        version = d.pop("Version")

        id = d.pop("Id", UNSET)

        api_policy = cls(
            statement=statement,
            version=version,
            id=id,
        )

        api_policy.additional_properties = d
        return api_policy

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
