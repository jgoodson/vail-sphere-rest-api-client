from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_storage_graph_data import ApiStorageGraphData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    length: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sl/api/usage/sphere/graph".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["length"] = length

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["ApiStorageGraphData"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiStorageGraphData.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["ApiStorageGraphData"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    length: Union[Unset, None, str] = UNSET,
) -> Response[List["ApiStorageGraphData"]]:
    """Get sphere usage data for the given time length

    Args:
        length (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ApiStorageGraphData']]
    """

    kwargs = _get_kwargs(
        client=client,
        length=length,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    length: Union[Unset, None, str] = UNSET,
) -> Optional[List["ApiStorageGraphData"]]:
    """Get sphere usage data for the given time length

    Args:
        length (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ApiStorageGraphData']
    """

    return sync_detailed(
        client=client,
        length=length,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    length: Union[Unset, None, str] = UNSET,
) -> Response[List["ApiStorageGraphData"]]:
    """Get sphere usage data for the given time length

    Args:
        length (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ApiStorageGraphData']]
    """

    kwargs = _get_kwargs(
        client=client,
        length=length,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    length: Union[Unset, None, str] = UNSET,
) -> Optional[List["ApiStorageGraphData"]]:
    """Get sphere usage data for the given time length

    Args:
        length (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ApiStorageGraphData']
    """

    return (
        await asyncio_detailed(
            client=client,
            length=length,
        )
    ).parsed
