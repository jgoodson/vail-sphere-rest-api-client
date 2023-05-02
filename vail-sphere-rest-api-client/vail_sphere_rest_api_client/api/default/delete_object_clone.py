from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    object_: str,
    storage: str,
    *,
    client: Client,
    version: Union[Unset, None, str] = UNSET,
    optional: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sl/api/buckets/{name}/objects/{object}/{storage}".format(
        client.base_url, name=name, object=object_, storage=storage
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["version"] = version

    params["optional"] = optional

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    object_: str,
    storage: str,
    *,
    client: Client,
    version: Union[Unset, None, str] = UNSET,
    optional: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ServerValidationErrorResponse]]:
    """Delete object clone

    Args:
        name (str):
        object_ (str):
        storage (str):
        version (Union[Unset, None, str]):
        optional (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        object_=object_,
        storage=storage,
        client=client,
        version=version,
        optional=optional,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    object_: str,
    storage: str,
    *,
    client: Client,
    version: Union[Unset, None, str] = UNSET,
    optional: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ServerValidationErrorResponse]]:
    """Delete object clone

    Args:
        name (str):
        object_ (str):
        storage (str):
        version (Union[Unset, None, str]):
        optional (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ServerValidationErrorResponse]
    """

    return sync_detailed(
        name=name,
        object_=object_,
        storage=storage,
        client=client,
        version=version,
        optional=optional,
    ).parsed


async def asyncio_detailed(
    name: str,
    object_: str,
    storage: str,
    *,
    client: Client,
    version: Union[Unset, None, str] = UNSET,
    optional: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ServerValidationErrorResponse]]:
    """Delete object clone

    Args:
        name (str):
        object_ (str):
        storage (str):
        version (Union[Unset, None, str]):
        optional (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        object_=object_,
        storage=storage,
        client=client,
        version=version,
        optional=optional,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    object_: str,
    storage: str,
    *,
    client: Client,
    version: Union[Unset, None, str] = UNSET,
    optional: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ServerValidationErrorResponse]]:
    """Delete object clone

    Args:
        name (str):
        object_ (str):
        storage (str):
        version (Union[Unset, None, str]):
        optional (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            name=name,
            object_=object_,
            storage=storage,
            client=client,
            version=version,
            optional=optional,
        )
    ).parsed
