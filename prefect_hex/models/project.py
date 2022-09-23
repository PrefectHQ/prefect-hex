# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2022-09-22T23:16:55+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, Field


class NextPageUrl(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: str = Field(
        ...,
        description="URL to fetch the next page of results for a paginated API request",
    )


class Offset(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: int = Field(..., description="Offset for paginated requests", ge=0)


class PageSize(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: int = Field(
        ...,
        description="Number of results to fetch per page for paginated requests",
        ge=1,
        le=100,
    )


class ProjectId(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: UUID = Field(
        ...,
        description="Unique ID for a Hex project",
    )


class ProjectRunStatus(Enum):
    """
    Current status of a project run.
    """

    pending = "PENDING"
    running = "RUNNING"
    errored = "ERRORED"
    completed = "COMPLETED"
    killed = "KILLED"
    unabletoallocatekernel = "UNABLE_TO_ALLOCATE_KERNEL"


class RunId(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: UUID = Field(
        ...,
        description="Unique ID for a run of a Hex project",
    )


class RunProjectRequestBody(BaseModel):
    class Config:
        extra = Extra.allow
        extra = Extra.forbid
        allow_mutation = False

    dry_run: Optional[bool] = Field(
        "false",
        alias="dryRun",
        description=(
            "If specified, perform a dry run without actually executing the project."
        ),
    )
    input_params: Optional[Dict[str, Any]] = Field(
        None,
        alias="inputParams",
        description="Optional input parameter value map for this project run.",
        example={"numeric_input_1": 123, "text_input_1": "Hello World"},
    )
    update_cache: Optional[bool] = Field(
        "false",
        alias="updateCache",
        description=(
            "When true, this run will update the cached state of the published app with"
            " the latest run results.\nAdditionally, any SQL cells that have caching"
            " enabled will be re-executed as part of this run. Note\nthat this cannot"
            " be set to true if custom input parameters are provided."
        ),
    )


class RunStatusUrl(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: str = Field(
        ..., description="URL to query the status of the project run via the Hex API"
    )


class RunUrl(BaseModel):

    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: str = Field(
        ...,
        description="URL to view the current progress of the project run in the Hex UI",
    )


class TraceId(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    __root__: str = Field(
        ...,
        description=(
            "Hex trace ID to identify an API request. Provide this value to hex support"
            " with any API issues you encounter"
        ),
    )


class TsoaErrorResponsePayload(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    reason: str
    trace_id: TraceId = Field(..., alias="traceId")


class ProjectRunResponsePayload(BaseModel):
    """
    Response format returned by the runProject endpoint
    """

    class Config:
        extra = Extra.allow
        extra = Extra.forbid
        allow_mutation = False

    project_id: ProjectId = Field(..., alias="projectId")
    run_id: RunId = Field(..., alias="runId")
    run_status_url: RunStatusUrl = Field(..., alias="runStatusUrl")
    run_url: RunUrl = Field(..., alias="runUrl")
    trace_id: TraceId = Field(..., alias="traceId")


class ProjectStatusResponsePayload(BaseModel):
    """
    Response format returned by the getRunStatus endpoint
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    elapsed_time: float = Field(
        ...,
        alias="elapsedTime",
        description="Total elapsed time for the project run in milliseconds",
    )
    end_time: datetime = Field(
        ...,
        alias="endTime",
        description="UTC timestamp of when the project run finished",
    )
    project_id: ProjectId = Field(..., alias="projectId")
    run_id: RunId = Field(..., alias="runId")
    run_url: RunUrl = Field(..., alias="runUrl")
    start_time: datetime = Field(
        ...,
        alias="startTime",
        description="UTC timestamp of when the project run started",
    )
    status: ProjectRunStatus
    trace_id: TraceId = Field(..., alias="traceId")


class ProjectRunsResponsePayload(BaseModel):
    """
    Response format returned by the getProjectRuns endpoint
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    next_page: NextPageUrl = Field(..., alias="nextPage")
    previous_page: NextPageUrl = Field(..., alias="previousPage")
    runs: List[ProjectStatusResponsePayload] = Field(
        ...,
        description=(
            "Array of run status payloads in the same format returned by the"
            " `GetRunStatus` endpoint"
        ),
    )
    trace_id: TraceId = Field(..., alias="traceId")
