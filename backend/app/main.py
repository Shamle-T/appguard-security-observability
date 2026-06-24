"""Backend application entry point placeholder."""

from fastapi import FastAPI

import app.models
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.errors import AppGuardException, appguard_exception_handler
from app.db.base import Base
from app.db.session import engine

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Security observability SaaS for web applications.",
)

app.add_exception_handler(AppGuardException, appguard_exception_handler)

app.include_router(api_router, prefix=settings.api_v1_prefix)


# fast API decorater
@app.on_event("startup")
def create_database_tables():
    # Base.metadata is SQLAlchemy’s collection of all table definitions it knows about.
    # It means that when we use import app.models, all of those data about the models are stored in Base.metadata
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def root_health_check():
    return {"status": "ok", "service": settings.app_name}
