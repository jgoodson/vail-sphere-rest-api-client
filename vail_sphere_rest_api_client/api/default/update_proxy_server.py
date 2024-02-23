from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_http_proxy import ApiHttpProxy
from ...models.api_http_proxy_response import ApiHttpProxyResponse
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApiHttpProxy,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/sl/api/proxy/global",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiHttpProxyResponse.from_dict(response.json())

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
) -> Response[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiHttpProxy,
) -> Response[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]:
    """Update a global network proxy configuration

    Args:
        body (ApiHttpProxy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiHttpProxy,
) -> Optional[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]:
    """Update a global network proxy configuration

    Args:
        body (ApiHttpProxy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiHttpProxyResponse, ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiHttpProxy,
) -> Response[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]:
    """Update a global network proxy configuration

    Args:
        body (ApiHttpProxy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiHttpProxy,
) -> Optional[Union[ApiHttpProxyResponse, ServerValidationErrorResponse]]:
    """Update a global network proxy configuration

    Args:
        body (ApiHttpProxy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiHttpProxyResponse, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
