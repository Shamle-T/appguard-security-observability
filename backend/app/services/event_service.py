from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.errors import AppGuardException
from app.models.application import Application
from app.models.event import Event
from app.schemas.event import EventCreate

# The route should not contain all the business logic. The route should receive the request, call the service, and return the response.


def create_event(db: Session, payload: EventCreate) -> Event:
    application = db.get(Application, payload.application_id)

    if application is None:
        raise AppGuardException(message="Application not found", status_code=404)

    if not application.is_active:
        raise AppGuardException(message="Application is inactive", status_code=400)
    event = Event(
        application_id=payload.application_id,
        event_type=payload.event_type,
        ip_address=payload.ip_address,
        user_identifier=payload.user_identifier,
        endpoint=payload.endpoint,
        timestamp=payload.timestamp or datetime.now(timezone.utc),
        event_metadata=payload.metadata or {},
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


# Pagination -
def list_events(db: Session, limit: int = 50, offset: int = 0) -> list[Event]:
    return (
        db.query(Event)
        .order_by(Event.timestamp.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
