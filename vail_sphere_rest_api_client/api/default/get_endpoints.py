from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_endpoint import ApiEndpoint
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sl/api/endpoints".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[List["ApiEndpoint"], ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiEndpoint.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ServerValidationErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[List["ApiEndpoint"], ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Union[List["ApiEndpoint"], ServerValidationErrorResponse]]:
    """List endpoints

    Args:
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['ApiEndpoint'], ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[List["ApiEndpoint"], ServerValidationErrorResponse]]:
    """List endpoints

    Args:
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['ApiEndpoint'], ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Union[List["ApiEndpoint"], ServerValidationErrorResponse]]:
    """List endpoints

    Args:
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['ApiEndpoint'], ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[List["ApiEndpoint"], ServerValidationErrorResponse]]:
    """List endpoints

    Args:
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['ApiEndpoint'], ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
        )
    ).parsed
