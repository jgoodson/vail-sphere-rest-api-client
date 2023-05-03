from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_token_challenge_parameters import ApiTokenChallengeParameters


T = TypeVar("T", bound="ApiToken")


@attr.s(auto_attribs=True)
class ApiToken:
    """
    Attributes:
        challenge_name (Union[Unset, str]): The challenge that must be passed first.
        challenge_parameters (Union[Unset, ApiTokenChallengeParameters]): The challenge parameters for the given
            challenge.
        session (Union[Unset, str]): Temporary session ID used to pass a challenge.  This is only populated if
            ChallengeName is populated.
        token (Union[Unset, str]): The JSON Web Token
        username (Union[Unset, str]): The user login name.
    """

    challenge_name: Union[Unset, str] = UNSET
    challenge_parameters: Union[Unset, "ApiTokenChallengeParameters"] = UNSET
    session: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge_name = self.challenge_name
        challenge_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.challenge_parameters, Unset):
            challenge_parameters = self.challenge_parameters.to_dict()

        session = self.session
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
        if token is not UNSET:
            field_dict["token"] = token
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_token_challenge_parameters import ApiTokenChallengeParameters

        d = src_dict.copy()
        challenge_name = d.pop("challengeName", UNSET)

        _challenge_parameters = d.pop("challengeParameters", UNSET)
        challenge_parameters: Union[Unset, ApiTokenChallengeParameters]
        if isinstance(_challenge_parameters, Unset):
            challenge_parameters = UNSET
        else:
            challenge_parameters = ApiTokenChallengeParameters.from_dict(_challenge_parameters)

        session = d.pop("session", UNSET)

        token = d.pop("token", UNSET)

        username = d.pop("username", UNSET)

        api_token = cls(
            challenge_name=challenge_name,
            challenge_parameters=challenge_parameters,
            session=session,
            token=token,
            username=username,
        )

        api_token.additional_properties = d
        return api_token

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
