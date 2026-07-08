from venv import create

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.event import Event
from app.schemas.event import EventCreate, EventListResponse, EventResponse
from app.services.event_service import create_event, list_events

router = APIRouter(prefix="/events", tags=["Events"])


# This function is used to convert a database Event object into a clean API response.
def to_event_response(event: Event) -> EventResponse:
    return EventResponse(
        id=event.id,
        application_id=event.application_id,
        event_type=event.event_type,
        ip_address=event.ip_address,
        user_identifier=event.user_identifier,
        endpoint=event.endpoint,
        timestamp=event.timestamp,
        metadata=event.event_metadata,
        created_at=event.created_at,
    )


# reponse_model is a FAST API keyword/parameter
@router.post("", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_security_event(payload: EventCreate, db: Session = Depends(get_db)):
    event = create_event(db=db, payload=payload)
    return to_event_response(event)


@router.get("", response_model=EventListResponse)
def get_events(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    events = list_events(db=db, limit=limit, offset=offset)

    return EventListResponse(
        events=[to_event_response(event) for event in events], count=len(events)
    )
