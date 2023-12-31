from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PolicyDocumentStatement")


@attr.s(auto_attribs=True)
class PolicyDocumentStatement:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)
    multi_statement: bool = attr.ib(False)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    def to_object(self) -> Dict[str, Any] | List[Any]:
        if self.multi_statement:
            statement_list: List[Any] = []
            statement_list.extend(self.additional_properties["statements"])
            return statement_list

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        policy_document_statement = cls()

        policy_document_statement.additional_properties = d
        return policy_document_statement
    
    @classmethod
    def from_object(cls: Type[T], src_obj: Dict[str, Any] | List[Any]) -> T:
        d = src_obj.copy()
        policy_document_statement = cls()

        if isinstance(d, dict):
            policy_document_statement.additional_properties = d
            policy_document_statement.multi_statement = False
        else:
            policy_document_statement.additional_properties = {"statements": d}
            policy_document_statement.multi_statement = True
        return policy_document_statement

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
