from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.api_cognito_user_password_reset import ApiCognitoUserPasswordReset
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: Client,
    json_body: ApiCognitoUserPasswordReset,
) -> Dict[str, Any]:
    url = "{}/sl/api/users/{username}/forgot_password".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ServerValidationErrorResponse]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ServerValidationErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
    json_body: ApiCognitoUserPasswordReset,
) -> Response[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        json_body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerValidationErrorResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Client,
    json_body: ApiCognitoUserPasswordReset,
) -> Optional[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        json_body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerValidationErrorResponse
    """

    return sync_detailed(
        username=username,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    json_body: ApiCognitoUserPasswordReset,
) -> Response[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        json_body (ApiCognitoUserPasswordReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerValidationErrorResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    json_body: ApiCognitoUserPasswordReset,
) -> Optional[ServerValidationErrorResponse]:
    """Reset the user's password

    Args:
        username (str):
        json_body (ApiCognitoUserPasswordReset):

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
            json_body=json_body,
        )
    ).parsed
