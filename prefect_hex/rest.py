"""
This is a module containing generic REST tasks.
"""

import json
from enum import Enum
from typing import TYPE_CHECKING, Any, Dict, Union

import httpx
from prefect import task
from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import BaseModel
else:
    from pydantic import BaseModel

if TYPE_CHECKING:
    from prefect_hex import HexCredentials


class HTTPMethod(Enum):
    """
    Available HTTP request methods.
    """

    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"


def serialize_model(obj: Any) -> Any:
    """
    Recursively serializes `pydantic.BaseModel` into JSON;
    returns original obj if not a `BaseModel`.

    Args:
        obj: Input object to serialize.

    Returns:
        Serialized version of object.
    """
    if isinstance(obj, list):
        return [serialize_model(o) for o in obj]
    elif isinstance(obj, Dict):
        return {k: serialize_model(v) for k, v in obj.items()}

    if isinstance(obj, BaseModel):
        obj = obj.dict()
    return obj


def strip_kwargs(**kwargs: Dict) -> Dict:
    """
    Recursively drops keyword arguments if value is None,
    and serializes any `pydantic.BaseModel` types.

    Args:
        **kwargs: Input keyword arguments.

    Returns:
        Stripped version of kwargs.
    """
    stripped_dict = {}
    for k, v in kwargs.items():
        v = serialize_model(v)
        if isinstance(v, dict):
            v = strip_kwargs(**v)
        if v is not None:
            stripped_dict[k] = v
    return stripped_dict or {}


@task
async def execute_endpoint(
    endpoint: str,
    hex_credentials: "HexCredentials",
    http_method: HTTPMethod = HTTPMethod.GET,
    params: Dict[str, Any] = None,
    json: Dict[str, Any] = None,
    **kwargs: Dict[str, Any],
) -> httpx.Response:
    """
    Generic function for executing REST endpoints.

    Args:
        endpoint: The endpoint route.
        hex_credentials: Credentials to use for authentication with Hex.
        http_method: Either GET, POST, PUT, DELETE, or PATCH.
        params: URL query parameters in the request.
        json: JSON serializable object to include in the body of the request.
        **kwargs: Additional keyword arguments to pass.

    Returns:
        The httpx.Response from interacting with the endpoint.

    Examples:
        Queries project runs for a given project ID.
        ```python
        from prefect import flow
        from prefect_hex import HexCredentials
        from prefect_hex.rest import execute_endpoint

        @flow
        def example_execute_endpoint_flow():
            endpoint = f"/project/5a8591dd-4039-49df-9202-96385ba3eff8/runs"
            hex_credentials = HexCredentials(token="a1b2c3d4")
            params = dict(limit=100)

            response = execute_endpoint(endpoint, hex_credentials, params=params)
            return response.json()

        example_execute_endpoint_flow()
        ```
    """
    if isinstance(http_method, HTTPMethod):
        http_method = http_method.value

    if params is not None:
        stripped_params = strip_kwargs(**params)
    else:
        stripped_params = None

    if json is not None:
        kwargs["json"] = strip_kwargs(**json)

    async with hex_credentials.get_client() as client:
        response = await getattr(client, http_method)(
            endpoint, params=stripped_params, **kwargs
        )

    return response


def _unpack_contents(response: httpx.Response) -> Union[Dict[str, Any], bytes]:
    """
    Helper method to unpack the contents from the httpx.Response,
    reporting errors in a helpful manner, if any.
    """
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise httpx.HTTPStatusError(
            response.json(), request=exc.request, response=exc.response
        ) from exc

    try:
        return response.json()
    except json.JSONDecodeError:
        return response.content
