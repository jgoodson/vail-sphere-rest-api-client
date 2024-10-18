from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_google_parameters import ApiGoogleParameters
from ...models.api_target_item_details import ApiTargetItemDetails
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
    item: str,
    *,
    body: ApiGoogleParameters,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/sl/api/targets/{id}/google/{item}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiTargetItemDetails.from_dict(response.json())

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
) -> Response[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    item: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiGoogleParameters,
) -> Response[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]:
    """Get supported functionality for a specific target item

    Args:
        id (str):
        item (str):
        body (ApiGoogleParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        item=item,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    item: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiGoogleParameters,
) -> Optional[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]:
    """Get supported functionality for a specific target item

    Args:
        id (str):
        item (str):
        body (ApiGoogleParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTargetItemDetails, ServerValidationErrorResponse]
    """

    return sync_detailed(
        id=id,
        item=item,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    item: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiGoogleParameters,
) -> Response[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]:
    """Get supported functionality for a specific target item

    Args:
        id (str):
        item (str):
        body (ApiGoogleParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        item=item,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    item: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiGoogleParameters,
) -> Optional[Union[ApiTargetItemDetails, ServerValidationErrorResponse]]:
    """Get supported functionality for a specific target item

    Args:
        id (str):
        item (str):
        body (ApiGoogleParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTargetItemDetails, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            item=item,
            client=client,
            body=body,
        )
    ).parsed
