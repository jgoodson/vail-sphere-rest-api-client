import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_audits import ApiAudits
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    username: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["username"] = username

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["marker"] = marker

    params["max-keys"] = max_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sl/api/reports/audit",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiAudits, ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiAudits.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ServerValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiAudits, ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Response[Union[ApiAudits, ServerValidationErrorResponse]]:
    """Get audit log data

    Args:
        username (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiAudits, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        start=start,
        end=end,
        marker=marker,
        max_keys=max_keys,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiAudits, ServerValidationErrorResponse]]:
    """Get audit log data

    Args:
        username (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiAudits, ServerValidationErrorResponse]
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
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Response[Union[ApiAudits, ServerValidationErrorResponse]]:
    """Get audit log data

    Args:
        username (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiAudits, ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        start=start,
        end=end,
        marker=marker,
        max_keys=max_keys,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    marker: Union[Unset, str] = UNSET,
    max_keys: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiAudits, ServerValidationErrorResponse]]:
    """Get audit log data

    Args:
        username (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        marker (Union[Unset, str]):
        max_keys (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiAudits, ServerValidationErrorResponse]
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
