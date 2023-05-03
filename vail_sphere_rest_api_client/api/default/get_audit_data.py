import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.handlers_audit_data_pagination import HandlersAuditDataPagination
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sl/api/reports/audit".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["username"] = username

    json_start: Union[Unset, None, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat() if start else None

    params["start"] = json_start

    json_end: Union[Unset, None, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat() if end else None

    params["end"] = json_end

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
) -> Optional[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = HandlersAuditDataPagination.from_dict(response.json())

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
) -> Response[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Response[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]:
    """Get audit log data from elasticsearch

    Args:
        username (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        username=username,
        start=start,
        end=end,
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
    username: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Optional[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]:
    """Get audit log data from elasticsearch

    Args:
        username (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HandlersAuditDataPagination, ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        username=username,
        start=start,
        end=end,
        marker=marker,
        max_keys=max_keys,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Response[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]:
    """Get audit log data from elasticsearch

    Args:
        username (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        username=username,
        start=start,
        end=end,
        marker=marker,
        max_keys=max_keys,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    marker: Union[Unset, None, str] = UNSET,
    max_keys: Union[Unset, None, int] = UNSET,
) -> Optional[Union[HandlersAuditDataPagination, ServerValidationErrorResponse]]:
    """Get audit log data from elasticsearch

    Args:
        username (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        marker (Union[Unset, None, str]):
        max_keys (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HandlersAuditDataPagination, ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            start=start,
            end=end,
            marker=marker,
            max_keys=max_keys,
        )
    ).parsed
