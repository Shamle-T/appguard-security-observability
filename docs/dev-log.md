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


## 23 June 2026 - Day 3

### Goal
Set up PostgreSQL with Docker Compose and connect the FastAPI backend to the database.

### Completed
- Added PostgreSQL service in Docker Compose
- Added backend Dockerfile
- Added backend service in Docker Compose
- Added SQLAlchemy database engine
- Added database session setup
- Added DATABASE_URL configuration
- Added database health check endpoint
- Verified `/api/v1/health/db`

### Notes
The backend now runs with PostgreSQL through Docker Compose. Inside Docker, the database host is `db`; outside Docker, it is `localhost`.

### Next
Create SQLAlchemy models for User, Workspace, App, Event, Alert, Incident, and AuditLog.


## 24 June 2026 - Day 4

### Goal
Create the initial SQLAlchemy database models for AppGuard.

### Completed
- Added SQLAlchemy Base
- Added timestamp mixin
- Created User model
- Created Workspace model
- Created WorkspaceMember model
- Created Application model
- Created APIKey model
- Created Event model
- Created Alert model
- Created Incident model
- Created AuditLog model
- Registered models in `app/models/__init__.py`
- Created tables automatically on backend startup
- Verified database connectivity through `/api/v1/health/db`

### Notes
The database schema v0 now supports the core AppGuard SaaS structure: users, workspaces, applications, API keys, security events, alerts, incidents, and audit logs.

### Next
Build the first event creation endpoint with validation so events can be posted and stored.
