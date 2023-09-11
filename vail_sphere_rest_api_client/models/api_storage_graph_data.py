from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_storage_graph_data_point import ApiStorageGraphDataPoint


T = TypeVar("T", bound="ApiStorageGraphData")


@attr.s(auto_attribs=True)
class ApiStorageGraphData:
    """
    Attributes:
        label (str): Dataset label
        data (Union[Unset, List['ApiStorageGraphDataPoint']]): Data points of storage used (percent)
        rate (Union[Unset, float]): Average growth rate of storage used
    """

    label: str
    data: Union[Unset, List["ApiStorageGraphDataPoint"]] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_storage_graph_data_point import ApiStorageGraphDataPoint

        d = src_dict.copy()
        label = d.pop("label")

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ApiStorageGraphDataPoint.from_dict(data_item_data)

            data.append(data_item)

        rate = d.pop("rate", UNSET)

        api_storage_graph_data = cls(
            label=label,
            data=data,
            rate=rate,
        )

        api_storage_graph_data.additional_properties = d
        return api_storage_graph_data

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
