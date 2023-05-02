from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.elasticsearch_storage_growth_data_point import ElasticsearchStorageGrowthDataPoint


T = TypeVar("T", bound="ElasticsearchStorageGrowthData")


@attr.s(auto_attribs=True)
class ElasticsearchStorageGrowthData:
    """
    Attributes:
        data (List['ElasticsearchStorageGrowthDataPoint']): Data points of storage used (percent)
        label (str): Dataset label
        rate (float): Average growth rate of storage used
    """

    data: List["ElasticsearchStorageGrowthDataPoint"]
    label: str
    rate: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        label = self.label
        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "label": label,
                "rate": rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.elasticsearch_storage_growth_data_point import ElasticsearchStorageGrowthDataPoint

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ElasticsearchStorageGrowthDataPoint.from_dict(data_item_data)

            data.append(data_item)

        label = d.pop("label")

        rate = d.pop("rate")

        elasticsearch_storage_growth_data = cls(
            data=data,
            label=label,
            rate=rate,
        )

        elasticsearch_storage_growth_data.additional_properties = d
        return elasticsearch_storage_growth_data

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
