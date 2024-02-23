from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.license_entitlement import LicenseEntitlement
from ...models.license_signed_entitlements import LicenseSignedEntitlements
from ...models.server_validation_error_response import ServerValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LicenseSignedEntitlements,
    signature: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["signature"] = signature

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/sl/api/entitlements",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[List["LicenseEntitlement"], ServerValidationErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = LicenseEntitlement.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
) -> Response[Union[List["LicenseEntitlement"], ServerValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LicenseSignedEntitlements,
    signature: Union[Unset, str] = UNSET,
) -> Response[Union[List["LicenseEntitlement"], ServerValidationErrorResponse]]:
    """Set entitlements

    Args:
        signature (Union[Unset, str]):
        body (LicenseSignedEntitlements):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['LicenseEntitlement'], ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        signature=signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LicenseSignedEntitlements,
    signature: Union[Unset, str] = UNSET,
) -> Optional[Union[List["LicenseEntitlement"], ServerValidationErrorResponse]]:
    """Set entitlements

    Args:
        signature (Union[Unset, str]):
        body (LicenseSignedEntitlements):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['LicenseEntitlement'], ServerValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        signature=signature,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LicenseSignedEntitlements,
    signature: Union[Unset, str] = UNSET,
) -> Response[Union[List["LicenseEntitlement"], ServerValidationErrorResponse]]:
    """Set entitlements

    Args:
        signature (Union[Unset, str]):
        body (LicenseSignedEntitlements):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['LicenseEntitlement'], ServerValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        signature=signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LicenseSignedEntitlements,
    signature: Union[Unset, str] = UNSET,
) -> Optional[Union[List["LicenseEntitlement"], ServerValidationErrorResponse]]:
    """Set entitlements

    Args:
        signature (Union[Unset, str]):
        body (LicenseSignedEntitlements):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['LicenseEntitlement'], ServerValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            signature=signature,
        )
    ).parsed
