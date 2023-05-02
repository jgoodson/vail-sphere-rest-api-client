from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_document_statement import PolicyDocumentStatement


T = TypeVar("T", bound="PolicyDocument")


@attr.s(auto_attribs=True)
class PolicyDocument:
    """
    Attributes:
        statement (PolicyDocumentStatement):
        version (str):
        id (Union[Unset, str]):
    """

    statement: "PolicyDocumentStatement"
    version: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statement = self.statement.to_dict()

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
        from ..models.policy_document_statement import PolicyDocumentStatement

        d = src_dict.copy()
        statement = PolicyDocumentStatement.from_dict(d.pop("Statement"))

        version = d.pop("Version")

        id = d.pop("Id", UNSET)

        policy_document = cls(
            statement=statement,
            version=version,
            id=id,
        )

        policy_document.additional_properties = d
        return policy_document

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
