from uuid import uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Workspace(Base, TimestampMixin):
    __tablename__ = "workspaces"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    owner_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True
    )

    # relationship(Name of the model which it connects to, back populates -> name of the relationship in the opposite model )
    owner = relationship("User", back_populates="owned_workspace")

    members = relationship(
        "WorkspaceMember", back_populates="workspace", cascade="all, delete-orphan"
    )

    applications = relationship(
        "Application", back_populates="workspace", cascade="all, delete-orphan"
    )

    incidents = relationship(
        "Incident", back_populates="workspace", cascade="all, delete-orphan"
    )

    audit_logs = relationship(
        "AuditLog", back_populates="workspace", cascade="all, delete-orphan"
    )
