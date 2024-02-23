from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_sphere_token_challenge_parameters import RestSphereTokenChallengeParameters


T = TypeVar("T", bound="RestSphereToken")


@_attrs_define
class RestSphereToken:
    """
    Attributes:
        challenge_name (Union[Unset, str]): The challenge that must be passed first.
        challenge_parameters (Union[Unset, RestSphereTokenChallengeParameters]): The challenge parameters for the given
            challenge.
        session (Union[Unset, str]): Temporary session ID used to pass a challenge.  This is only populated if
            ChallengeName is populated.
        sphere (Union[Unset, str]): The Sphere that this token is valid for.
        token (Union[Unset, str]): The JSON Web Token
        username (Union[Unset, str]): The user login name.
    """

    challenge_name: Union[Unset, str] = UNSET
    challenge_parameters: Union[Unset, "RestSphereTokenChallengeParameters"] = UNSET
    session: Union[Unset, str] = UNSET
    sphere: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge_name = self.challenge_name

        challenge_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.challenge_parameters, Unset):
            challenge_parameters = self.challenge_parameters.to_dict()

        session = self.session

        sphere = self.sphere

        token = self.token

        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_name is not UNSET:
            field_dict["challengeName"] = challenge_name
        if challenge_parameters is not UNSET:
            field_dict["challengeParameters"] = challenge_parameters
        if session is not UNSET:
            field_dict["session"] = session
        if sphere is not UNSET:
            field_dict["sphere"] = sphere
        if token is not UNSET:
            field_dict["token"] = token
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_sphere_token_challenge_parameters import RestSphereTokenChallengeParameters

        d = src_dict.copy()
        challenge_name = d.pop("challengeName", UNSET)

        _challenge_parameters = d.pop("challengeParameters", UNSET)
        challenge_parameters: Union[Unset, RestSphereTokenChallengeParameters]
        if isinstance(_challenge_parameters, Unset):
            challenge_parameters = UNSET
        else:
            challenge_parameters = RestSphereTokenChallengeParameters.from_dict(_challenge_parameters)

        session = d.pop("session", UNSET)

        sphere = d.pop("sphere", UNSET)

        token = d.pop("token", UNSET)

        username = d.pop("username", UNSET)

        rest_sphere_token = cls(
            challenge_name=challenge_name,
            challenge_parameters=challenge_parameters,
            session=session,
            sphere=sphere,
            token=token,
            username=username,
        )

        rest_sphere_token.additional_properties = d
        return rest_sphere_token

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
