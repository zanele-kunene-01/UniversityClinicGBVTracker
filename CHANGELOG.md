# CHANGELOG

### Added
- Created `Report` model using Pydantic for data validation.
- Developed `InMemoryReportRepository` with full CRUD support.
- Implemented `ReportService` for business logic:
  - Input validation
  - Storage through repository pattern
- Built RESTful API endpoints with FastAPI:
  - `POST /api/reports` — Create a new report
  - `GET /api/reports` — List all reports
  - `GET /api/reports/{id}` — Retrieve report by ID
  - `DELETE /api/reports/{id}` — Delete a report
- Auto-generated API documentation using Swagger UI (`/docs`).
- Included OpenAPI export at `/docs/openapi.json`.

### Tests
- Added unit tests for `ReportService` (create, retrieve).
- Added integration tests for API endpoints using FastAPI's TestClient.

### Fixed
- Fixed `500 Internal Server Error` when deleting a non-existent report.
- Improved error messaging for empty descriptions (400 Bad Request).
- Resolved crash on invalid JSON input in `POST /api/reports`.

### Documentation
- Added API documentation via Swagger (OpenAPI 3.0).
- Linked GitHub commits to issues for traceability:
  - `Close #21: Implement report service`
  - `Close #22: Add in-memory ReportRepository`
  - `Close #23: Expose /api/reports routes`
  - `Close #24: Create Report model schema`
  - `Close #27: Write unit test for create_report`
- Kanban board updated with service/API workflow.

---

##  Tags

- `feature`: Initial API endpoints and services
- `bug`: Critical fix for report deletion error
- `doc`: Swagger/OpenAPI documentation added
