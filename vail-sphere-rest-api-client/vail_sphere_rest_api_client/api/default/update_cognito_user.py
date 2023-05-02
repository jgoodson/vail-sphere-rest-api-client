from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...models.users_user import UsersUser
from ...models.users_user_patch import UsersUserPatch
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: Client,
    json_body: UsersUserPatch,
) -> Dict[str, Any]:
    url = "{}/sl/api/users/{username}".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ServerValidationErrorResponse, UsersUser]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersUser.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ServerValidationErrorResponse, UsersUser]]:
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
    json_body: UsersUserPatch,
) -> Response[Union[ServerValidationErrorResponse, UsersUser]]:
    """Update a user

    Args:
        username (str):
        json_body (UsersUserPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ServerValidationErrorResponse, UsersUser]]
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
    json_body: UsersUserPatch,
) -> Optional[Union[ServerValidationErrorResponse, UsersUser]]:
    """Update a user

    Args:
        username (str):
        json_body (UsersUserPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ServerValidationErrorResponse, UsersUser]
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
    json_body: UsersUserPatch,
) -> Response[Union[ServerValidationErrorResponse, UsersUser]]:
    """Update a user

    Args:
        username (str):
        json_body (UsersUserPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ServerValidationErrorResponse, UsersUser]]
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
    json_body: UsersUserPatch,
) -> Optional[Union[ServerValidationErrorResponse, UsersUser]]:
    """Update a user

    Args:
        username (str):
        json_body (UsersUserPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ServerValidationErrorResponse, UsersUser]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            json_body=json_body,
        )
    ).parsed
