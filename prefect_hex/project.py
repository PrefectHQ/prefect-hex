"""
This is a module containing tasks for interacting with
Hex projects
"""

from typing import Dict, Optional

from prefect import task

from prefect_hex import HexCredentials
from prefect_hex.models import project as models
from prefect_hex.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def run_project(
    project_id: str,
    hex_credentials: HexCredentials,
    input_params: Optional[Dict] = None,
    dry_run: bool = False,
    update_cache: bool = False,
) -> models.ProjectRunResponsePayload:  # pragma: no cover
    """
    Trigger a run of the latest published version of a project.

    Args:
        project_id:
            Project ID to run.
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
        Information about the triggered project run.
    """  # noqa
    endpoint = f"/project/{project_id}/run"  # noqa

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.POST,
        json=models.RunProjectRequestBody(
            dryRun=dry_run, inputParams=input_params, updateCache=update_cache
        ).dict(by_alias=True),
    )

    contents = _unpack_contents(response)
    return models.ProjectRunResponsePayload.parse_obj(contents)


@task
async def get_run_status(
    project_id: str,
    run_id: str,
    hex_credentials: HexCredentials,
) -> models.ProjectStatusResponsePayload:  # pragma: no cover
    """
    Get the status of a project run.

    Args:
        project_id:
            Project ID associated with the run to get the status of.
        run_id:
            Run ID of the run to get the status of.
        hex_credentials:
            Credentials to use for authentication with Hex.

    Returns:
        Information about the requested run.
    """  # noqa
    endpoint = f"/project/{project_id}/run/{run_id}"  # noqa

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.GET,
    )

    contents = _unpack_contents(response)
    return models.ProjectStatusResponsePayload.parse_obj(contents)


@task
async def cancel_run(
    project_id: str,
    run_id: str,
    hex_credentials: HexCredentials,
) -> None:  # pragma: no cover
    """
    Cancel a project run.

    Args:
        project_id:
            Project ID associated with the run to cancel.
        run_id:
            Run ID of the run to cancel.
        hex_credentials:
            Credentials to use for authentication with Hex.
    """  # noqa
    endpoint = f"/project/{project_id}/run/{run_id}"  # noqa

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.DELETE,
    )

    # Handles any errors returned by the API
    _unpack_contents(response)


@task
async def get_project_runs(
    project_id: str,
    hex_credentials: HexCredentials,
    limit: Optional[models.PageSize] = None,
    offset: Optional[models.Offset] = None,
    status_filter: Optional[models.ProjectRunStatus] = None,
) -> models.ProjectRunsResponsePayload:  # pragma: no cover
    """
    Get the status of the API-triggered runs of a project.

    Args:
        project_id:
            Project ID to get runs for.
        hex_credentials:
            Credentials to use for authentication with Hex.
        limit:
            Number of results to fetch per page for paginated requests.
        offset:
            Offset for paginated requests.
        status_filter:
            Current status of a project run.

    Returns:
        Details of all the retrieved runs.
    """  # noqa
    endpoint = f"/project/{project_id}/runs"  # noqa

    params = {
        "limit": limit,
        "offset": offset,
        "statusFilter": status_filter.value if status_filter is not None else None,
    }

    response = await execute_endpoint.fn(
        endpoint,
        hex_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response)
    return models.ProjectRunsResponsePayload.parse_obj(contents)
