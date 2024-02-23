from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoint_registration import ApiEndpointRegistration
from ...models.handlers_node_registration_info import HandlersNodeRegistrationInfo
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApiEndpointRegistration,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/sl/api/sphere/endpoints",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = HandlersNodeRegistrationInfo.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiEndpointRegistration,
) -> Response[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]:
    """Register this endpoint

    Args:
        body (ApiEndpointRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]
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
    body: ApiEndpointRegistration,
) -> Optional[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]:
    """Register this endpoint

    Args:
        body (ApiEndpointRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiEndpointRegistration,
) -> Response[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]:
    """Register this endpoint

    Args:
        body (ApiEndpointRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiEndpointRegistration,
) -> Optional[Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]]:
    """Register this endpoint

    Args:
        body (ApiEndpointRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HandlersNodeRegistrationInfo, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
