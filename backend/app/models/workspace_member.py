from uuid import uuid4

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class WorkspaceMember(Base, TimestampMixin):
    __tablename__ = "workspace_members"

    __table_args__ = (
        UniqueConstraint(
            "user_id", "workspace_id", name="uq_workspace_member_user_workspace"
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True
    )

    workspace_id: Mapped[str] = mapped_column(
        ForeignKey("workspaces.id"), nullable=False, index=True
    )

    role: Mapped[str] = mapped_column(String(50), nullable=False, default="viewer")

    user = relationship("User", back_populates="memberships")

    workspace = relationship("Workspace", back_populates="members")
