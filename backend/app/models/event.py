from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


def utc_now():
    return datetime.now(timezone.utc)


class Event(Base, TimestampMixin):
    __tablename__ = "events"

    __table_args__ = (
        Index(
            "ix_events_app_type_timestamp", "application_id", "event_type", "timestamp"
        ),
        Index(
            "ix_events_app_ip_timestamp", "application_id", "ip_address", "timestamp"
        ),
        Index(
            "ix_events_app_user_timestamp",
            "application_id",
            "user_identifier",
            "timestamp",
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    application_id: Mapped[str] = mapped_column(
        ForeignKey("applications.id"), nullable=False, index=True
    )

    event_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    ip_address: Mapped[str | None] = mapped_column(
        String(45), nullable=True, index=True
    )

    user_identifier: Mapped[str | None] = mapped_column(
        String(255), nullable=True, index=True
    )

    endpoint: Mapped[str | None] = mapped_column(String(500), nullable=True)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False, index=True
    )

    event_metadata: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    application = relationship("Application", back_populates="events")

    alerts = relationship("Alert", back_populates="event")
