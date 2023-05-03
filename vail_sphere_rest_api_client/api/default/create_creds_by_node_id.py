from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_node_credentials import ApiNodeCredentials
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    nodeid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sl/api/creds/{nodeid}".format(client.base_url, nodeid=nodeid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ApiNodeCredentials, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ApiNodeCredentials.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ServerValidationErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ApiNodeCredentials, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    nodeid: str,
    *,
    client: Client,
) -> Response[Union[ApiNodeCredentials, ServerValidationErrorResponse]]:
    """Create the credentials for the node.

    Args:
        nodeid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiNodeCredentials, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        nodeid=nodeid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    nodeid: str,
    *,
    client: Client,
) -> Optional[Union[ApiNodeCredentials, ServerValidationErrorResponse]]:
    """Create the credentials for the node.

    Args:
        nodeid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiNodeCredentials, ServerValidationErrorResponse]
    """

    return sync_detailed(
        nodeid=nodeid,
        client=client,
    ).parsed


async def asyncio_detailed(
    nodeid: str,
    *,
    client: Client,
) -> Response[Union[ApiNodeCredentials, ServerValidationErrorResponse]]:
    """Create the credentials for the node.

    Args:
        nodeid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiNodeCredentials, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        nodeid=nodeid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nodeid: str,
    *,
    client: Client,
) -> Optional[Union[ApiNodeCredentials, ServerValidationErrorResponse]]:
    """Create the credentials for the node.

    Args:
        nodeid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiNodeCredentials, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            nodeid=nodeid,
            client=client,
        )
    ).parsed
