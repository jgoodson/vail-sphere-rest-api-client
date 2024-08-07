from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_rule_apply import ApiRuleApply
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_destinations import ApiDestinations
    from ..models.api_rule_schedule import ApiRuleSchedule


T = TypeVar("T", bound="ApiRule")


@_attrs_define
class ApiRule:
    """
    Attributes:
        name (str):
        apply (Union[Unset, ApiRuleApply]):  Default: ApiRuleApply.ALL.
        deletion (Union[Unset, bool]): Deletion removes clones not in the specified destinations
        destinations (Union[Unset, ApiDestinations]):
        exclude (Union[Unset, str]): Regular expression that must not match the object name
        expiration (Union[Unset, bool]): Expiration is a deletion without destinations that deletes the object version
        include (Union[Unset, str]): Regular expression that must match the object name
        noncurrent_versions (Union[Unset, int]): How many noncurrent versions for the rule to keep. Once this number is
            exceeded, the oldest noncurrent version is expired.
        schedule (Union[Unset, ApiRuleSchedule]):
    """

    name: str
    apply: Union[Unset, ApiRuleApply] = ApiRuleApply.ALL
    deletion: Union[Unset, bool] = UNSET
    destinations: Union[Unset, "ApiDestinations"] = UNSET
    exclude: Union[Unset, str] = UNSET
    expiration: Union[Unset, bool] = UNSET
    include: Union[Unset, str] = UNSET
    noncurrent_versions: Union[Unset, int] = UNSET
    schedule: Union[Unset, "ApiRuleSchedule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        apply: Union[Unset, str] = UNSET
        if not isinstance(self.apply, Unset):
            apply = self.apply.value

        deletion = self.deletion

        destinations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = self.destinations.to_dict()

        exclude = self.exclude

        expiration = self.expiration

        include = self.include

        noncurrent_versions = self.noncurrent_versions

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if apply is not UNSET:
            field_dict["apply"] = apply
        if deletion is not UNSET:
            field_dict["deletion"] = deletion
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if include is not UNSET:
            field_dict["include"] = include
        if noncurrent_versions is not UNSET:
            field_dict["noncurrentVersions"] = noncurrent_versions
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_destinations import ApiDestinations
        from ..models.api_rule_schedule import ApiRuleSchedule

        d = src_dict.copy()
        name = d.pop("name")

        _apply = d.pop("apply", UNSET)
        apply: Union[Unset, ApiRuleApply]
        if isinstance(_apply, Unset):
            apply = UNSET
        else:
            apply = ApiRuleApply(_apply)

        deletion = d.pop("deletion", UNSET)

        _destinations = d.pop("destinations", UNSET)
        destinations: Union[Unset, ApiDestinations]
        if isinstance(_destinations, Unset):
            destinations = UNSET
        else:
            destinations = ApiDestinations.from_dict(_destinations)

        exclude = d.pop("exclude", UNSET)

        expiration = d.pop("expiration", UNSET)

        include = d.pop("include", UNSET)

        noncurrent_versions = d.pop("noncurrentVersions", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ApiRuleSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ApiRuleSchedule.from_dict(_schedule)

        api_rule = cls(
            name=name,
            apply=apply,
            deletion=deletion,
            destinations=destinations,
            exclude=exclude,
            expiration=expiration,
            include=include,
            noncurrent_versions=noncurrent_versions,
            schedule=schedule,
        )

        api_rule.additional_properties = d
        return api_rule

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
