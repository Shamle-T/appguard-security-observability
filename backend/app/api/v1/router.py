"""Versioned API router placeholder."""

from fastapi import APIRouter

from app.api.v1.routes import events, health

api_router = APIRouter()

# health.py files' router variable
api_router.include_router(health.router)
api_router.include_router(events.router)
