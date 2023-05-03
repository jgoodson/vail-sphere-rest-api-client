from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_logsets import ApiLogsets
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sl/api/logsets".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["marker"] = marker

    params["max-keys"] = max_keys

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
) -> Optional[Union[ApiLogsets, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiLogsets.from_dict(response.json())

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
) -> Response[Union[ApiLogsets, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Response[Union[ApiLogsets, ServerValidationErrorResponse]]:
    """List all logsets stored in Vail's AWS S3 Sphere bucket

    Args:
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLogsets, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        marker=marker,
        max_keys=max_keys,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ApiLogsets, ServerValidationErrorResponse]]:
    """List all logsets stored in Vail's AWS S3 Sphere bucket

    Args:
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLogsets, ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        marker=marker,
        max_keys=max_keys,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Response[Union[ApiLogsets, ServerValidationErrorResponse]]:
    """List all logsets stored in Vail's AWS S3 Sphere bucket

    Args:
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLogsets, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        marker=marker,
        max_keys=max_keys,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ApiLogsets, ServerValidationErrorResponse]]:
    """List all logsets stored in Vail's AWS S3 Sphere bucket

    Args:
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLogsets, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marker=marker,
            max_keys=max_keys,
        )
    ).parsed
