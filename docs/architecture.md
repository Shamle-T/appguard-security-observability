# Architecture

Client App / Demo Simulator
        ↓
AppGuard Ingestion API
        ↓
API Key Validation
        ↓
Event Storage in PostgreSQL
        ↓
Detection Rules
        ↓
Alerts + Incidents
        ↓
Dashboard API
        ↓
React Dashboard


1. A registered app sends a security event to AppGuard.
2. The event includes an API key.
3. AppGuard validates the API key.
4. If valid, the event is stored in PostgreSQL.
5. Detection rules check whether the event is suspicious.
6. If suspicious behaviour is found, AppGuard creates an alert.
7. Related alerts can be grouped into incidents.
8. Dashboard APIs expose recent events, alerts, severity counts, risk score, and incident timeline.
9. React dashboard displays this information to the user.
