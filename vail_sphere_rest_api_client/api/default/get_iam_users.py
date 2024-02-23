from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_iam_users import ApiIAMUsers
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    account: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sl/api/iam/users/{account}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiIAMUsers, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiIAMUsers.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ServerValidationErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiIAMUsers, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiIAMUsers, ServerValidationErrorResponse]]:
    """List all IAM users for the specific account

    Args:
        account (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiIAMUsers, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiIAMUsers, ServerValidationErrorResponse]]:
    """List all IAM users for the specific account

    Args:
        account (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiIAMUsers, ServerValidationErrorResponse]
    """

    return sync_detailed(
        account=account,
        client=client,
    ).parsed


async def asyncio_detailed(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiIAMUsers, ServerValidationErrorResponse]]:
    """List all IAM users for the specific account

    Args:
        account (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiIAMUsers, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiIAMUsers, ServerValidationErrorResponse]]:
    """List all IAM users for the specific account

    Args:
        account (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiIAMUsers, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            account=account,
            client=client,
        )
    ).parsed
