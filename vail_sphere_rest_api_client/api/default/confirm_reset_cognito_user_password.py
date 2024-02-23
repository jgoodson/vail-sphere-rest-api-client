from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_cognito_user_password_reset import ApiCognitoUserPasswordReset
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    body: ApiCognitoUserPasswordReset,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/sl/api/users/{username}/forgot_password",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ServerValidationErrorResponse]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ServerValidationErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiCognitoUserPasswordReset,
) -> Response[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerValidationErrorResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiCognitoUserPasswordReset,
) -> Optional[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerValidationErrorResponse
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiCognitoUserPasswordReset,
) -> Response[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerValidationErrorResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiCognitoUserPasswordReset,
) -> Optional[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerValidationErrorResponse
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
        )
    ).parsed
