"""Health schema placeholder."""
# Creates the shape of the response

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str
    environment: str
