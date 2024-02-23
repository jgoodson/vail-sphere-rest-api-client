from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_credentials_challenge_responses import RestCredentialsChallengeResponses


T = TypeVar("T", bound="RestCredentials")


@_attrs_define
class RestCredentials:
    """
    Attributes:
        username (str): The user login name.
        challenge_name (Union[Unset, str]): The challenge to pass.
        challenge_responses (Union[Unset, RestCredentialsChallengeResponses]): The responses for the given challenge.
            This is required when challengeName is supplied.
        otp (Union[Unset, str]): One-time password for multi-factor authentication. This is only used for backends that
            don't support MFA challenges (e.g. BlackPearl)'.
        password (Union[Unset, str]): The password for the user.  This is only required when initially trying to create
            a token and not when responding to a challenge.
        session (Union[Unset, str]): The session ID used to pass the challenge.  This is required when challengeName is
            supplied.
    """

    username: str
    challenge_name: Union[Unset, str] = UNSET
    challenge_responses: Union[Unset, "RestCredentialsChallengeResponses"] = UNSET
    otp: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    session: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        challenge_name = self.challenge_name

        challenge_responses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.challenge_responses, Unset):
            challenge_responses = self.challenge_responses.to_dict()

        otp = self.otp

        password = self.password

        session = self.session

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if challenge_name is not UNSET:
            field_dict["challengeName"] = challenge_name
        if challenge_responses is not UNSET:
            field_dict["challengeResponses"] = challenge_responses
        if otp is not UNSET:
            field_dict["otp"] = otp
        if password is not UNSET:
            field_dict["password"] = password
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_credentials_challenge_responses import RestCredentialsChallengeResponses

        d = src_dict.copy()
        username = d.pop("username")

        challenge_name = d.pop("challengeName", UNSET)

        _challenge_responses = d.pop("challengeResponses", UNSET)
        challenge_responses: Union[Unset, RestCredentialsChallengeResponses]
        if isinstance(_challenge_responses, Unset):
            challenge_responses = UNSET
        else:
            challenge_responses = RestCredentialsChallengeResponses.from_dict(_challenge_responses)

        otp = d.pop("otp", UNSET)

        password = d.pop("password", UNSET)

        session = d.pop("session", UNSET)

        rest_credentials = cls(
            username=username,
            challenge_name=challenge_name,
            challenge_responses=challenge_responses,
            otp=otp,
            password=password,
            session=session,
        )

        rest_credentials.additional_properties = d
        return rest_credentials

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
