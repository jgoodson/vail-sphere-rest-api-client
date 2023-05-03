from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_summary_logging_process_status import ApiSummaryLoggingProcessStatus

T = TypeVar("T", bound="ApiSummary")


@attr.s(auto_attribs=True)
class ApiSummary:
    """
    Attributes:
        average_object_size (int): Average Size of Managed Objects
        logging_process_status (ApiSummaryLoggingProcessStatus): Logging Process Status
        object_count (int): Total Number of Managed Objects
        total_managed (int): Bytes of Total Managed storage
        total_transactions (int): Total Number of Transactions
    """

    average_object_size: int
    logging_process_status: ApiSummaryLoggingProcessStatus
    object_count: int
    total_managed: int
    total_transactions: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average_object_size = self.average_object_size
        logging_process_status = self.logging_process_status.value

        object_count = self.object_count
        total_managed = self.total_managed
        total_transactions = self.total_transactions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "averageObjectSize": average_object_size,
                "loggingProcessStatus": logging_process_status,
                "objectCount": object_count,
                "totalManaged": total_managed,
                "totalTransactions": total_transactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        average_object_size = d.pop("averageObjectSize")

        logging_process_status = ApiSummaryLoggingProcessStatus(d.pop("loggingProcessStatus"))

        object_count = d.pop("objectCount")

        total_managed = d.pop("totalManaged")

        total_transactions = d.pop("totalTransactions")

        api_summary = cls(
            average_object_size=average_object_size,
            logging_process_status=logging_process_status,
            object_count=object_count,
            total_managed=total_managed,
            total_transactions=total_transactions,
        )

        api_summary.additional_properties = d
        return api_summary

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
