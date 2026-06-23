# Data Model v0

## User
- id
- email
- hashed_password
- full_name
- created_at

## Workspace
- id
- name
- owner_id
- created_at

## WorkspaceMember
- id
- user_id
- workspace_id
- role: admin | analyst | viewer

## App
- id
- workspace_id
- name
- description
- created_at

## APIKey
- id
- app_id
- key_hash
- prefix
- is_active
- created_at
- revoked_at

## Event
- id
- app_id
- event_type
- ip_address
- user_identifier
- endpoint
- occurred_at
- metadata_json
- created_at

## Alert
- id
- app_id
- event_id
- incident_id
- severity: low | medium | high | critical
- title
- description
- rule_name
- status
- created_at

## Incident
- id
- workspace_id
- title
- severity
- status: open | investigating | resolved
- created_at
- resolved_at

## AuditLog
- id
- workspace_id
- actor_user_id
- action
- target_type
- target_id
- metadata_json
- created_at
