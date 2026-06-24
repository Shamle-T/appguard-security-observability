from uuid import uuid4

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Alert(Base, TimestampMixin):
    __tablename__ = "alerts"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    application_id: Mapped[str] = mapped_column(
        ForeignKey("applications.id"), nullable=False, index=True
    )

    event_id: Mapped[str | None] = mapped_column(
        ForeignKey("events.id"), nullable=True, index=True
    )

    incident_id: Mapped[str | None] = mapped_column(
        ForeignKey("incidents.id"), nullable=True, index=True
    )

    severity: Mapped[str] = mapped_column(
        String(50), nullable=False, default="low", index=True
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    rule_name: Mapped[str] = mapped_column(String(100), nullable=False)

    status: Mapped[str] = mapped_column(
        String(50), nullable=False, default="open", index=True
    )

    application = relationship("Application", back_populates="alerts")

    event = relationship("Event", back_populates="alerts")

    incident = relationship("Incident", back_populates="alerts")
