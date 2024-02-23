from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_iam_user_key import ApiIAMUserKey
from ...models.api_iam_user_key_update import ApiIAMUserKeyUpdate
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    account: str,
    username: str,
    id: str,
    *,
    body: ApiIAMUserKeyUpdate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/sl/api/iam/users/{account}/{username}/keys/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiIAMUserKey, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiIAMUserKey.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ServerValidationErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiIAMUserKey, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account: str,
    username: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiIAMUserKeyUpdate,
) -> Response[Union[ApiIAMUserKey, ServerValidationErrorResponse]]:
    """Modify an IAM key

    Args:
        account (str):
        username (str):
        id (str):
        body (ApiIAMUserKeyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiIAMUserKey, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        username=username,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account: str,
    username: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiIAMUserKeyUpdate,
) -> Optional[Union[ApiIAMUserKey, ServerValidationErrorResponse]]:
    """Modify an IAM key

    Args:
        account (str):
        username (str):
        id (str):
        body (ApiIAMUserKeyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiIAMUserKey, ServerValidationErrorResponse]
    """

    return sync_detailed(
        account=account,
        username=username,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account: str,
    username: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiIAMUserKeyUpdate,
) -> Response[Union[ApiIAMUserKey, ServerValidationErrorResponse]]:
    """Modify an IAM key

    Args:
        account (str):
        username (str):
        id (str):
        body (ApiIAMUserKeyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiIAMUserKey, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        username=username,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account: str,
    username: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiIAMUserKeyUpdate,
) -> Optional[Union[ApiIAMUserKey, ServerValidationErrorResponse]]:
    """Modify an IAM key

    Args:
        account (str):
        username (str):
        id (str):
        body (ApiIAMUserKeyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiIAMUserKey, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            account=account,
            username=username,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
