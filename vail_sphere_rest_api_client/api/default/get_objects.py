from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_list_objects_result import ApiListObjectsResult
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    client: Client,
    prefix: Union[Unset, None, str] = UNSET,
    delimiter: Union[Unset, None, str] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    versions: Union[Unset, None, bool] = UNSET,
    version_id_marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sl/api/buckets/{name}/objects".format(client.base_url, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["prefix"] = prefix

    params["delimiter"] = delimiter

    params["marker"] = marker

    params["versions"] = versions

    params["version-id-marker"] = version_id_marker

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
) -> Optional[Union[ApiListObjectsResult, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiListObjectsResult.from_dict(response.json())

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
    *, client: Client, response: httpx.Response
) -> Response[Union[ApiListObjectsResult, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Client,
    prefix: Union[Unset, None, str] = UNSET,
    delimiter: Union[Unset, None, str] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    versions: Union[Unset, None, bool] = UNSET,
    version_id_marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Response[Union[ApiListObjectsResult, ServerValidationErrorResponse]]:
    """List all objects in the given bucket

    Args:
        name (str):
        prefix (Union[Unset, None, str]):
        delimiter (Union[Unset, None, str]):
        marker (Union[Unset, None, str]):
        versions (Union[Unset, None, bool]):
        version_id_marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListObjectsResult, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        prefix=prefix,
        delimiter=delimiter,
        marker=marker,
        versions=versions,
        version_id_marker=version_id_marker,
        max_keys=max_keys,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: Client,
    prefix: Union[Unset, None, str] = UNSET,
    delimiter: Union[Unset, None, str] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    versions: Union[Unset, None, bool] = UNSET,
    version_id_marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ApiListObjectsResult, ServerValidationErrorResponse]]:
    """List all objects in the given bucket

    Args:
        name (str):
        prefix (Union[Unset, None, str]):
        delimiter (Union[Unset, None, str]):
        marker (Union[Unset, None, str]):
        versions (Union[Unset, None, bool]):
        version_id_marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListObjectsResult, ServerValidationErrorResponse]
    """

    return sync_detailed(
        name=name,
        client=client,
        prefix=prefix,
        delimiter=delimiter,
        marker=marker,
        versions=versions,
        version_id_marker=version_id_marker,
        max_keys=max_keys,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Client,
    prefix: Union[Unset, None, str] = UNSET,
    delimiter: Union[Unset, None, str] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    versions: Union[Unset, None, bool] = UNSET,
    version_id_marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Response[Union[ApiListObjectsResult, ServerValidationErrorResponse]]:
    """List all objects in the given bucket

    Args:
        name (str):
        prefix (Union[Unset, None, str]):
        delimiter (Union[Unset, None, str]):
        marker (Union[Unset, None, str]):
        versions (Union[Unset, None, bool]):
        version_id_marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListObjectsResult, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        prefix=prefix,
        delimiter=delimiter,
        marker=marker,
        versions=versions,
        version_id_marker=version_id_marker,
        max_keys=max_keys,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: Client,
    prefix: Union[Unset, None, str] = UNSET,
    delimiter: Union[Unset, None, str] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    versions: Union[Unset, None, bool] = UNSET,
    version_id_marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ApiListObjectsResult, ServerValidationErrorResponse]]:
    """List all objects in the given bucket

    Args:
        name (str):
        prefix (Union[Unset, None, str]):
        delimiter (Union[Unset, None, str]):
        marker (Union[Unset, None, str]):
        versions (Union[Unset, None, bool]):
        version_id_marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListObjectsResult, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            prefix=prefix,
            delimiter=delimiter,
            marker=marker,
            versions=versions,
            version_id_marker=version_id_marker,
            max_keys=max_keys,
        )
    ).parsed
