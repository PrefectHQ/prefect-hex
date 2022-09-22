"""
This is a module containing tasks for interacting with:
Hex project
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: openapi.yaml
# Updated at: 2022-09-22T23:16:55.466405

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_hex import HexCredentials
from prefect_hex.models import project as models  # noqa
from prefect_hex.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def run_project(
    project_id: str,
    hex_credentials: "HexCredentials",
    input_params: Dict = None,
    dry_run: bool = False,
    update_cache: bool = False,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Trigger a run of the latest published version of a project.

    Args:
        project_id:
            Project id used in formatting the endpoint URL.
        hex_credentials:
            Credentials to use for authentication with Hex.
        input_params:
            Optional input parameter value map for this project run, e.g.
            ```
            {"text_input_1": "Hello World", "numeric_input_1": 123}
            ```
        dry_run:
            If specified, perform a dry run without actually executing the project.
        update_cache:
            When true, this run will update the cached state of the published app
            with the latest run results. Additionally, any SQL cells
            that have caching enabled will be re-executed as part of
            this run. Note that this cannot be set to true if custom
            input parameters are provided.

    Returns:
        Upon success, a dict of the response. </br>- `project_id: "models.ProjectId"`</br>- `run_id: "models.RunId"`</br>- `run_url: "models.RunUrl"`</br>- `run_status_url: "models.RunStatusUrl"`</br>- `trace_id: "models.TraceId"`</br>

    <h4>API Endpoint:</h4>
    `/project/{project_id}/run`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    endpoint = "/project/{project_id}/run"  # noqa

    responses = {}

    params = {
        "project_id": project_id,
    }

    json_payload = {
        "input_params": input_params,
        "dry_run": dry_run,
        "update_cache": update_cache,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def get_run_status(
    project_id: str,
    run_id: str,
    hex_credentials: "HexCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the status of a project run.

    Args:
        project_id:
            Project id used in formatting the endpoint URL.
        run_id:
            Run id used in formatting the endpoint URL.
        hex_credentials:
            Credentials to use for authentication with Hex.

    Returns:
        Upon success, a dict of the response. </br>- `project_id: "models.ProjectId"`</br>- `run_id: "models.RunId"`</br>- `run_url: "models.RunUrl"`</br>- `status: "models.ProjectRunStatus"`</br>- `start_time: str`</br>- `end_time: str`</br>- `elapsed_time: str`</br>- `trace_id: "models.TraceId"`</br>

    <h4>API Endpoint:</h4>
    `/project/{project_id}/run/{run_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    endpoint = "/project/{project_id}/run/{run_id}"  # noqa

    responses = {}

    params = {
        "project_id": project_id,
        "run_id": run_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def cancel_run(
    project_id: str,
    run_id: str,
    hex_credentials: "HexCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Cancel a project run.

    Args:
        project_id:
            Project id used in formatting the endpoint URL.
        run_id:
            Run id used in formatting the endpoint URL.
        hex_credentials:
            Credentials to use for authentication with Hex.

    Returns:
        Upon success, an empty dict.

    <h4>API Endpoint:</h4>
    `/project/{project_id}/run/{run_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    endpoint = "/project/{project_id}/run/{run_id}"  # noqa

    responses = {}

    params = {
        "project_id": project_id,
        "run_id": run_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def get_project_runs(
    project_id: str,
    hex_credentials: "HexCredentials",
    limit: "models.PageSize" = None,
    offset: "models.Offset" = None,
    status_filter: "models.ProjectRunStatus" = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the status of the API-triggered runs of a project.

    Args:
        project_id:
            Project id used in formatting the endpoint URL.
        hex_credentials:
            Credentials to use for authentication with Hex.
        limit:
            Number of results to fetch per page for paginated requests.
        offset:
            Offset for paginated requests.
        status_filter:
            Current status of a project run.

    Returns:
        Upon success, a dict of the response. </br>- `runs: List["models.ProjectStatusResponsePayload"]`</br>- `next_page: str`</br>- `previous_page: str`</br>- `trace_id: "models.TraceId"`</br>

    <h4>API Endpoint:</h4>
    `/project/{project_id}/runs`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    endpoint = "/project/{project_id}/runs"  # noqa

    responses = {}

    params = {
        "project_id": project_id,
        "limit": limit,
        "offset": offset,
        "status_filter": status_filter,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
