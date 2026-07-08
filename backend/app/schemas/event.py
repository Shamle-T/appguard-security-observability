from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

EventType = Literal[
    "logic_success",
    "failed_login",
    "api_request",
    "suspicious_action",
    "password_reset",
    "privilege_change",
]


class EventCreate(BaseModel):
    application_id: str = Field(..., description="ID of the registered application")
    event_type: EventType
    ip_address: str | None = Field(default=None, max_length=45)
    user_identifier: str | None = Field(default=None, max_length=255)
    endpoint: str | None = Field(default=None, max_length=500)
    timestamp: datetime | None = None
    metadata: dict[str, Any] | None = Field(
        default_factory=dict
    )  # default_factory = dict, means to create an empty dictionary


class EventResponse(BaseModel):
    id: str
    application_id: str
    event_type: str
    ip_address: str | None
    user_identifier: str | None
    endpoint: str | None
    timestamp: datetime
    metadata: dict[str, Any] | None
    created_at: datetime


class EventListResponse(BaseModel):
    events: list[EventResponse]
    count: int
