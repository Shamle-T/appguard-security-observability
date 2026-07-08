from app.db.session import SessionLocal
from app.models.application import Application
from app.models.user import User
from app.models.workspace import Workspace
from app.models.workspace_member import WorkspaceMember


def seed_dev_data():
    db = SessionLocal()

    try:
        existing_user = db.query(User).filter(User.email == "demo@appguard.dev").first()

        if existing_user:
            existing_app = (
                db.query(Application)
                .filter(Application.name == "Demo E-commerce API")
                .first()
            )

            print("Dev data already exists.")

            if existing_app:
                print(f"Application ID: {existing_app.id}")

            return

        user = User(
            email="demo@appguard.dev",
            hashed_password="not_used_yet",
            full_name="Demo User",
        )

        db.add(user)
        db.flush()

        workspace = Workspace(name="Demo Workspace", owner_id=user.id)

        db.add(workspace)
        db.flush()

        member = WorkspaceMember(
            user_id=user.id, workspace_id=workspace.id, role="admin"
        )

        db.add(member)

        application = Application(
            workspace_id=workspace.id,
            name="Demo E-commerce API",
            description="Development application used for testing event ingestion.",
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        print("Dev data created successfully.")
        print(f"User email: {user.email}")
        print(f"Workspace ID: {workspace.id}")
        print(f"Application ID: {application.id}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_dev_data()
