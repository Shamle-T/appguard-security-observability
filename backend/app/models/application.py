from uuid import uuid4

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

# This represents a client application connected to AppGuard.


class Application(Base, TimestampMixin):
    __tablename__ = "applications"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    workspace_id: Mapped[str] = mapped_column(
        ForeignKey("workspaces.id"), nullable=False, index=True
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    workspace = relationship("Workspace", back_populates="applications")

    api_keys = relationship(
        "APIKey", back_populates="application", cascade="all, delete-orphan"
    )

    events = relationship(
        "Event", back_populates="application", cascade="all, delete-orphan"
    )

    alerts = relationship(
        "Alert", back_populates="application", cascade="all, delete-orphan"
    )
