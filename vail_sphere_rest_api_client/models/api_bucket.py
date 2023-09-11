import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_bucket_control import ApiBucketControl
from ..models.api_bucket_versioning import ApiBucketVersioning
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_acl import ApiACL
    from ..models.api_retention import ApiRetention
    from ..models.policy_document import PolicyDocument


T = TypeVar("T", bound="ApiBucket")


@attr.s(auto_attribs=True)
class ApiBucket:
    """
    Attributes:
        created (datetime.datetime): A timestamp of when the bucket was created.
        name (str): The bucket's name
        acls (Union[Unset, List['ApiACL']]): User and group ACLs
        block_public_acls (Union[Unset, bool]): True if public access control lists for this bucket and its objects are
            blocked
        block_public_policy (Union[Unset, bool]): True if public policies for this bucket are blocked
        compress (Union[Unset, bool]): True if compression should be attempted for all clones of objects stored in the
            bucket Default: True.
        control (Union[Unset, ApiBucketControl]): Bucket ownership control
        default_retention (Union[Unset, ApiRetention]):
        encrypt (Union[Unset, bool]): True if contents are encrypted
        ignore_public_acls (Union[Unset, bool]): True if public access control lists for this bucket and its objects are
            ignored
        lifecycle (Union[Unset, str]): The ID of the bucket's lifecycle
        linked_storage (Union[Unset, str]): Cloud or BlackPearl storage to use for linking
        locking (Union[Unset, bool]): True if object locking is enabled
        owner (Union[Unset, str]): The bucket's owner
        policy (Union[Unset, PolicyDocument]):
        restore (Union[Unset, bool]): True if automatic restore is enabled
        restrict_public_buckets (Union[Unset, bool]): True if public policies for this bucket are restricted
        versioning (Union[Unset, ApiBucketVersioning]): Bucket versioning status
    """

    created: datetime.datetime
    name: str
    acls: Union[Unset, List["ApiACL"]] = UNSET
    block_public_acls: Union[Unset, bool] = UNSET
    block_public_policy: Union[Unset, bool] = UNSET
    compress: Union[Unset, bool] = True
    control: Union[Unset, ApiBucketControl] = UNSET
    default_retention: Union[Unset, "ApiRetention"] = UNSET
    encrypt: Union[Unset, bool] = UNSET
    ignore_public_acls: Union[Unset, bool] = UNSET
    lifecycle: Union[Unset, str] = UNSET
    linked_storage: Union[Unset, str] = UNSET
    locking: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    policy: Union[Unset, "PolicyDocument"] = UNSET
    restore: Union[Unset, bool] = UNSET
    restrict_public_buckets: Union[Unset, bool] = UNSET
    versioning: Union[Unset, ApiBucketVersioning] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created.isoformat()

        name = self.name
        acls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acls, Unset):
            acls = []
            for acls_item_data in self.acls:
                acls_item = acls_item_data.to_dict()

                acls.append(acls_item)

        block_public_acls = self.block_public_acls
        block_public_policy = self.block_public_policy
        compress = self.compress
        control: Union[Unset, str] = UNSET
        if not isinstance(self.control, Unset):
            control = self.control.value

        default_retention: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_retention, Unset):
            default_retention = self.default_retention.to_dict()

        encrypt = self.encrypt
        ignore_public_acls = self.ignore_public_acls
        lifecycle = self.lifecycle
        linked_storage = self.linked_storage
        locking = self.locking
        owner = self.owner
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        restore = self.restore
        restrict_public_buckets = self.restrict_public_buckets
        versioning: Union[Unset, str] = UNSET
        if not isinstance(self.versioning, Unset):
            versioning = self.versioning.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "name": name,
            }
        )
        if acls is not UNSET:
            field_dict["acls"] = acls
        if block_public_acls is not UNSET:
            field_dict["blockPublicAcls"] = block_public_acls
        if block_public_policy is not UNSET:
            field_dict["blockPublicPolicy"] = block_public_policy
        if compress is not UNSET:
            field_dict["compress"] = compress
        if control is not UNSET:
            field_dict["control"] = control
        if default_retention is not UNSET:
            field_dict["defaultRetention"] = default_retention
        if encrypt is not UNSET:
            field_dict["encrypt"] = encrypt
        if ignore_public_acls is not UNSET:
            field_dict["ignorePublicAcls"] = ignore_public_acls
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if linked_storage is not UNSET:
            field_dict["linkedStorage"] = linked_storage
        if locking is not UNSET:
            field_dict["locking"] = locking
        if owner is not UNSET:
            field_dict["owner"] = owner
        if policy is not UNSET:
            field_dict["policy"] = policy
        if restore is not UNSET:
            field_dict["restore"] = restore
        if restrict_public_buckets is not UNSET:
            field_dict["restrictPublicBuckets"] = restrict_public_buckets
        if versioning is not UNSET:
            field_dict["versioning"] = versioning

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_acl import ApiACL
        from ..models.api_retention import ApiRetention
        from ..models.policy_document import PolicyDocument

        d = src_dict.copy()
        created = isoparse(d.pop("created"))

        name = d.pop("name")

        acls = []
        _acls = d.pop("acls", UNSET)
        for acls_item_data in _acls or []:
            acls_item = ApiACL.from_dict(acls_item_data)

            acls.append(acls_item)

        block_public_acls = d.pop("blockPublicAcls", UNSET)

        block_public_policy = d.pop("blockPublicPolicy", UNSET)

        compress = d.pop("compress", UNSET)

        _control = d.pop("control", UNSET)
        control: Union[Unset, ApiBucketControl]
        if isinstance(_control, Unset):
            control = UNSET
        else:
            control = ApiBucketControl(_control)

        _default_retention = d.pop("defaultRetention", UNSET)
        default_retention: Union[Unset, ApiRetention]
        if isinstance(_default_retention, Unset):
            default_retention = UNSET
        else:
            default_retention = ApiRetention.from_dict(_default_retention)

        encrypt = d.pop("encrypt", UNSET)

        ignore_public_acls = d.pop("ignorePublicAcls", UNSET)

        lifecycle = d.pop("lifecycle", UNSET)

        linked_storage = d.pop("linkedStorage", UNSET)

        locking = d.pop("locking", UNSET)

        owner = d.pop("owner", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, PolicyDocument]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PolicyDocument.from_dict(_policy)

        restore = d.pop("restore", UNSET)

        restrict_public_buckets = d.pop("restrictPublicBuckets", UNSET)

        _versioning = d.pop("versioning", UNSET)
        versioning: Union[Unset, ApiBucketVersioning]
        if isinstance(_versioning, Unset):
            versioning = UNSET
        else:
            versioning = ApiBucketVersioning(_versioning)

        api_bucket = cls(
            created=created,
            name=name,
            acls=acls,
            block_public_acls=block_public_acls,
            block_public_policy=block_public_policy,
            compress=compress,
            control=control,
            default_retention=default_retention,
            encrypt=encrypt,
            ignore_public_acls=ignore_public_acls,
            lifecycle=lifecycle,
            linked_storage=linked_storage,
            locking=locking,
            owner=owner,
            policy=policy,
            restore=restore,
            restrict_public_buckets=restrict_public_buckets,
            versioning=versioning,
        )

        api_bucket.additional_properties = d
        return api_bucket

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
