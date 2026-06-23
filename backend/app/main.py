"""Backend application entry point placeholder."""

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.errors import AppGuardException, appguard_exception_handler

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Security observability SaaS for web applications.",
)

app.add_exception_handler(AppGuardException, appguard_exception_handler)

app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/health")
def root_health_check():
    return {"status": "ok", "service": settings.app_name}
