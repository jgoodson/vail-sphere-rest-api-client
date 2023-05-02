from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_object import ApiObject
    from ..models.worker_common_prefix_result import WorkerCommonPrefixResult


T = TypeVar("T", bound="ApiListObjectsResult")


@attr.s(auto_attribs=True)
class ApiListObjectsResult:
    """
    Attributes:
        max_keys (int): Maximum number of entries returned in a page
        name (str): Bucket name
        common_prefixes (Union[Unset, List['WorkerCommonPrefixResult']]): If a delimiter is specified, this is the
            analogue of folders
        contents (Union[Unset, List['ApiObject']]): List of object versions
        delimiter (Union[Unset, str]): Delimiter used in the query
        is_truncated (Union[Unset, bool]): Indicates there are additional entries
        marker (Union[Unset, str]): Marker specified in the query
        next_marker (Union[Unset, str]): Marker to use for next page (if isTruncated)
        next_version_id_marker (Union[Unset, str]): Version ID narker to use for next page (if isTruncated)
        prefix (Union[Unset, str]): Prefix used in the query
        version_id_marker (Union[Unset, str]): Version ID marker specified in the query
        versions (Union[Unset, bool]): Indicates version data is present
    """

    max_keys: int
    name: str
    common_prefixes: Union[Unset, List["WorkerCommonPrefixResult"]] = UNSET
    contents: Union[Unset, List["ApiObject"]] = UNSET
    delimiter: Union[Unset, str] = UNSET
    is_truncated: Union[Unset, bool] = UNSET
    marker: Union[Unset, str] = UNSET
    next_marker: Union[Unset, str] = UNSET
    next_version_id_marker: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    version_id_marker: Union[Unset, str] = UNSET
    versions: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_keys = self.max_keys
        name = self.name
        common_prefixes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.common_prefixes, Unset):
            common_prefixes = []
            for common_prefixes_item_data in self.common_prefixes:
                common_prefixes_item = common_prefixes_item_data.to_dict()

                common_prefixes.append(common_prefixes_item)

        contents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contents, Unset):
            contents = []
            for contents_item_data in self.contents:
                contents_item = contents_item_data.to_dict()

                contents.append(contents_item)

        delimiter = self.delimiter
        is_truncated = self.is_truncated
        marker = self.marker
        next_marker = self.next_marker
        next_version_id_marker = self.next_version_id_marker
        prefix = self.prefix
        version_id_marker = self.version_id_marker
        versions = self.versions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxKeys": max_keys,
                "name": name,
            }
        )
        if common_prefixes is not UNSET:
            field_dict["commonPrefixes"] = common_prefixes
        if contents is not UNSET:
            field_dict["contents"] = contents
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter
        if is_truncated is not UNSET:
            field_dict["isTruncated"] = is_truncated
        if marker is not UNSET:
            field_dict["marker"] = marker
        if next_marker is not UNSET:
            field_dict["nextMarker"] = next_marker
        if next_version_id_marker is not UNSET:
            field_dict["nextVersionIDMarker"] = next_version_id_marker
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if version_id_marker is not UNSET:
            field_dict["versionIDMarker"] = version_id_marker
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_object import ApiObject
        from ..models.worker_common_prefix_result import WorkerCommonPrefixResult

        d = src_dict.copy()
        max_keys = d.pop("maxKeys")

        name = d.pop("name")

        common_prefixes = []
        _common_prefixes = d.pop("commonPrefixes", UNSET)
        for common_prefixes_item_data in _common_prefixes or []:
            common_prefixes_item = WorkerCommonPrefixResult.from_dict(common_prefixes_item_data)

            common_prefixes.append(common_prefixes_item)

        contents = []
        _contents = d.pop("contents", UNSET)
        for contents_item_data in _contents or []:
            contents_item = ApiObject.from_dict(contents_item_data)

            contents.append(contents_item)

        delimiter = d.pop("delimiter", UNSET)

        is_truncated = d.pop("isTruncated", UNSET)

        marker = d.pop("marker", UNSET)

        next_marker = d.pop("nextMarker", UNSET)

        next_version_id_marker = d.pop("nextVersionIDMarker", UNSET)

        prefix = d.pop("prefix", UNSET)

        version_id_marker = d.pop("versionIDMarker", UNSET)

        versions = d.pop("versions", UNSET)

        api_list_objects_result = cls(
            max_keys=max_keys,
            name=name,
            common_prefixes=common_prefixes,
            contents=contents,
            delimiter=delimiter,
            is_truncated=is_truncated,
            marker=marker,
            next_marker=next_marker,
            next_version_id_marker=next_version_id_marker,
            prefix=prefix,
            version_id_marker=version_id_marker,
            versions=versions,
        )

        api_list_objects_result.additional_properties = d
        return api_list_objects_result

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
