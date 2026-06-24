"""Health route placeholder."""

# Creates the end point that returns the earlier created shape in schema health.py

from fastapi import APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.db.session import engine
from app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


# The use of response model means - The response from this route should follow the HealthResponse schema.
# Create a GET endpoint at the router's base path using the below line ("")
@router.get("", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )


@router.get("/db")
def database_health_check():
    try:
        # Uses the db link to establish a connection
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"status": "ok", "database": "connected"}

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            defaults={
                "status": "error",
                "database": "not connected",
                "message": str(exc),
            },
        )
