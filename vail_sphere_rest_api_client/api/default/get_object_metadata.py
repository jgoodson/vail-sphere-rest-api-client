from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_object_metadata import ApiObjectMetadata
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    object_: str,
    *,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sl/api/buckets/{name}/objects/{object_}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiObjectMetadata, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiObjectMetadata.from_dict(response.json())

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
) -> Response[Union[ApiObjectMetadata, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    object_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[Unset, str] = UNSET,
) -> Response[Union[ApiObjectMetadata, ServerValidationErrorResponse]]:
    """Get object metadata

    Args:
        name (str):
        object_ (str):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiObjectMetadata, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        object_=object_,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    object_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiObjectMetadata, ServerValidationErrorResponse]]:
    """Get object metadata

    Args:
        name (str):
        object_ (str):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiObjectMetadata, ServerValidationErrorResponse]
    """

    return sync_detailed(
        name=name,
        object_=object_,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    name: str,
    object_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[Unset, str] = UNSET,
) -> Response[Union[ApiObjectMetadata, ServerValidationErrorResponse]]:
    """Get object metadata

    Args:
        name (str):
        object_ (str):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiObjectMetadata, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        object_=object_,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    object_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiObjectMetadata, ServerValidationErrorResponse]]:
    """Get object metadata

    Args:
        name (str):
        object_ (str):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiObjectMetadata, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            name=name,
            object_=object_,
            client=client,
            version=version,
        )
    ).parsed
