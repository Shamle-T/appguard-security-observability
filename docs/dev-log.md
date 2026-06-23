# Dev Log

# appguard-security-observability
Backend/cloud SaaS platform for ingesting security events, detecting suspicious activity, and managing alerts/incidents.
# Development Log

## 21 June 2026 - Day 1

### Goal
Set up the AppGuard project foundation, architecture, repo structure, and MVP scope.

### Completed
- Created project repository
- Drafted project architecture
- Defined MVP features
- Created initial folder structure
- Drafted data model v0
- Drafted API contract v0

### Notes
AppGuard will be built as a modular monolith first. The focus is backend/cloud engineering, with security observability as the domain.

### Next
Set up FastAPI backend skeleton, health check endpoint, config structure, and error handling pattern.


## 22 June 2026 - Day 2

### Goal
Set up the FastAPI backend skeleton with clean structure, config, health check, and basic error handling.

### Completed
- Created backend folder structure
- Added FastAPI application entry point
- Added API v1 router
- Added health check endpoint
- Added config system with pydantic-settings
- Added basic custom exception pattern
- Verified `/health`, `/api/v1/health`, and `/docs`

### Notes
The backend is now ready for database integration and PostgreSQL setup.

### Next
Set up PostgreSQL using Docker Compose and connect the backend to the database.
