from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_capacity_summary import ApiCapacitySummary


T = TypeVar("T", bound="ApiBlackPearlStatus")


@attr.s(auto_attribs=True)
class ApiBlackPearlStatus:
    """
    Attributes:
        active_jobs (int): Active jobs on the BlackPearl
        buckets (int): Total BlackPearl buckets
        cache_total (int): Cache capacity in bytes
        cache_used (int): Cache used in bytes
        capacity_summary (List['ApiCapacitySummary']): Capacity summaries
        database_total (int): Database capacity in bytes
        database_used (int): Database used in bytes
        name (str): BlackPearl name
        serial_number (str): BlackPearl Serial Number
        id (Union[Unset, str]): BlackPearl identifier
    """

    active_jobs: int
    buckets: int
    cache_total: int
    cache_used: int
    capacity_summary: List["ApiCapacitySummary"]
    database_total: int
    database_used: int
    name: str
    serial_number: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_jobs = self.active_jobs
        buckets = self.buckets
        cache_total = self.cache_total
        cache_used = self.cache_used
        capacity_summary = []
        for capacity_summary_item_data in self.capacity_summary:
            capacity_summary_item = capacity_summary_item_data.to_dict()

            capacity_summary.append(capacity_summary_item)

        database_total = self.database_total
        database_used = self.database_used
        name = self.name
        serial_number = self.serial_number
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activeJobs": active_jobs,
                "buckets": buckets,
                "cacheTotal": cache_total,
                "cacheUsed": cache_used,
                "capacitySummary": capacity_summary,
                "databaseTotal": database_total,
                "databaseUsed": database_used,
                "name": name,
                "serialNumber": serial_number,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_capacity_summary import ApiCapacitySummary

        d = src_dict.copy()
        active_jobs = d.pop("activeJobs")

        buckets = d.pop("buckets")

        cache_total = d.pop("cacheTotal")

        cache_used = d.pop("cacheUsed")

        capacity_summary = []
        _capacity_summary = d.pop("capacitySummary")
        for capacity_summary_item_data in _capacity_summary:
            capacity_summary_item = ApiCapacitySummary.from_dict(capacity_summary_item_data)

            capacity_summary.append(capacity_summary_item)

        database_total = d.pop("databaseTotal")

        database_used = d.pop("databaseUsed")

        name = d.pop("name")

        serial_number = d.pop("serialNumber")

        id = d.pop("id", UNSET)

        api_black_pearl_status = cls(
            active_jobs=active_jobs,
            buckets=buckets,
            cache_total=cache_total,
            cache_used=cache_used,
            capacity_summary=capacity_summary,
            database_total=database_total,
            database_used=database_used,
            name=name,
            serial_number=serial_number,
            id=id,
        )

        api_black_pearl_status.additional_properties = d
        return api_black_pearl_status

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
