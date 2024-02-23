from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_message_update import ApiMessageUpdate
from ...models.api_messages import ApiMessages
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ApiMessageUpdate,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["marker"] = marker

    params["max-keys"] = max_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/sl/api/messages",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiMessages, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiMessages.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiMessages, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiMessageUpdate,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Response[Union[ApiMessages, ServerValidationErrorResponse]]:
    """Update all messages

    Args:
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):
        body (ApiMessageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiMessages, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        marker=marker,
        max_keys=max_keys,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiMessageUpdate,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiMessages, ServerValidationErrorResponse]]:
    """Update all messages

    Args:
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):
        body (ApiMessageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiMessages, ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        marker=marker,
        max_keys=max_keys,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiMessageUpdate,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Response[Union[ApiMessages, ServerValidationErrorResponse]]:
    """Update all messages

    Args:
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):
        body (ApiMessageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiMessages, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        marker=marker,
        max_keys=max_keys,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiMessageUpdate,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiMessages, ServerValidationErrorResponse]]:
    """Update all messages

    Args:
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):
        body (ApiMessageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiMessages, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            marker=marker,
            max_keys=max_keys,
        )
    ).parsed
