from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_node_credentials import ApiNodeCredentials
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    nodeid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/sl/api/creds/{nodeid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    client: Union[AuthenticatedClient, Client],
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    nodeid: str,
    *,
    client: Union[AuthenticatedClient, Client],
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
    client: Union[AuthenticatedClient, Client],
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nodeid: str,
    *,
    client: Union[AuthenticatedClient, Client],
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
