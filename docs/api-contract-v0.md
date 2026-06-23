# API Contract v0

## Auth
POST /auth/register
POST /auth/login
GET /auth/me

## Workspaces
POST /workspaces
GET /workspaces
GET /workspaces/{workspace_id}

## Apps
POST /workspaces/{workspace_id}/apps
GET /workspaces/{workspace_id}/apps

## API Keys
POST /apps/{app_id}/api-keys
GET /apps/{app_id}/api-keys
PATCH /api-keys/{key_id}/revoke

## Event Ingestion
POST /ingest/events

Headers:
X-AppGuard-Key: <api_key>

Example event:
{
  "event_type": "failed_login",
  "ip_address": "192.168.1.20",
  "user_identifier": "user@example.com",
  "endpoint": "/login",
  "timestamp": "2026-06-21T10:30:00Z",
  "metadata": {
    "reason": "invalid_password",
    "user_agent": "Chrome"
  }
}

## Events
GET /events
GET /events/{event_id}

## Alerts
GET /alerts
GET /alerts/{alert_id}
PATCH /alerts/{alert_id}/status

## Incidents
GET /incidents
POST /incidents
PATCH /incidents/{incident_id}/status

## Dashboard
GET /dashboard/summary
GET /dashboard/recent-events
GET /dashboard/recent-alerts
GET /dashboard/severity-counts
GET /dashboard/timeline
