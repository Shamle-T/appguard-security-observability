# AppGuard

AppGuard is a backend/cloud SaaS platform for security observability in web applications.

## Project Purpose

Web applications generate many security-relevant events such as login attempts, failed logins, API activity, password resets, and privilege changes. AppGuard provides a platform to ingest these events, detect suspicious behaviour, create alerts/incidents, and display them in a dashboard.

## Why This Project Exists

This project is built to demonstrate backend engineering, cloud deployment, CI/CD, database design, testing, and security-aware software design.

## Tech Stack

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- React
- Docker
- Docker Compose
- Pytest
- GitHub Actions

## Architecture

Client App / Demo Simulator → Ingestion API → API Key Validation → Event Storage → Detection Rules → Alerts/Incidents → Dashboard API → React Dashboard

## MVP Features

- [ ] User registration and login
- [ ] JWT authentication
- [ ] Role-based access control: Admin, Analyst, Viewer
- [ ] Workspace creation
- [ ] Application registration inside workspaces
- [ ] API key generation and revocation
- [ ] Security event ingestion endpoint
- [ ] Event storage in PostgreSQL
- [ ] Repeated failed login detection
- [ ] Suspicious request burst detection
- [ ] Alert creation
- [ ] Incident workflow: open, investigating, resolved
- [ ] Audit logs
- [ ] Dashboard summary API
- [ ] React dashboard
- [ ] Demo simulator
- [ ] Docker Compose setup
- [ ] Pytest test suite
- [ ] GitHub Actions CI
- [ ] Deployment

## Out of Scope

- Kubernetes
- Microservices
- Machine learning detection
- Full SIEM features
- Complex notification systems
- Perfect UI design
- Multi-cloud deployment

## Development Log

See `docs/dev-log.md`.
