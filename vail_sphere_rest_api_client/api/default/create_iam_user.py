from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_iam_user import ApiIAMUser
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    account: str,
    username: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sl/api/iam/users/{account}/{username}".format(client.base_url, account=account, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ApiIAMUser, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiIAMUser.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ServerValidationErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ServerValidationErrorResponse.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ApiIAMUser, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account: str,
    username: str,
    *,
    client: Client,
) -> Response[Union[ApiIAMUser, ServerValidationErrorResponse]]:
    """Create a new IAM user

    Args:
        account (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiIAMUser, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        username=username,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account: str,
    username: str,
    *,
    client: Client,
) -> Optional[Union[ApiIAMUser, ServerValidationErrorResponse]]:
    """Create a new IAM user

    Args:
        account (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiIAMUser, ServerValidationErrorResponse]
    """

    return sync_detailed(
        account=account,
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    account: str,
    username: str,
    *,
    client: Client,
) -> Response[Union[ApiIAMUser, ServerValidationErrorResponse]]:
    """Create a new IAM user

    Args:
        account (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiIAMUser, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        username=username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account: str,
    username: str,
    *,
    client: Client,
) -> Optional[Union[ApiIAMUser, ServerValidationErrorResponse]]:
    """Create a new IAM user

    Args:
        account (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiIAMUser, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            account=account,
            username=username,
            client=client,
        )
    ).parsed