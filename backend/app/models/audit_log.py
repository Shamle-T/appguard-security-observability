from uuid import uuid4

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    workspace_id: Mapped[str | None] = mapped_column(
        ForeignKey("workspaces.id"), nullable=True, index=True
    )

    actor_user_id: Mapped[str | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, index=True
    )

    action: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    target_type: Mapped[str | None] = mapped_column(String(100), nullable=True)

    target_id: Mapped[str | None] = mapped_column(String(36), nullable=True)

    details: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    workspace = relationship("Workspace", back_populates="audit_logs")

    actor_user = relationship("User", back_populates="audit_logs")
