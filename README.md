# UniversityClinicGBVTracker
This project aims to develop a system for tracking gender-based violence (GBV) cases reported by students at a university clinic. The system will provide a secure and confidential platform for reporting, managing, and analyzing GBV cases.
The University Clinic GBV Tracker is a secure and confidential platform designed to help students report gender-based violence (GBV) incidents. The system will enable students to report cases safely, allow clinic staff to manage and track these cases efficiently, and provide tools for data analysis to identify trends and generate reports. Key components include a web application for user interaction, a database for storing case and user information, an authentication service for secure access, and API services for data handling. The system will ensure data security and privacy, complying with relevant regulations to protect sensitive information.

https://github.com/zanele-kunene-01/UniversityClinicGBVTracker/blob/main/Agile%20Planning%20Document.md

https://github.com/zanele-kunene-01/UniversityClinicGBVTracker/blob/main/SPECIFICATION.md SPECIFICATION.md

https://github.com/zanele-kunene-01/UniversityClinicGBVTracker/blob/main/ARCHITECTURE.md ARCHITECTURE.md

https://github.com/zanele-kunene-01/UniversityClinicGBVTracker/blob/main/SYSTEM_REQUIREMENTS.md

# Specifications

**Domain**
University Health Services

**Problem Statement**
The purpose of this system is to provide a secure and confidential platform for students to report gender-based violence (GBV) incidents to the university clinic. The system will help in managing and analyzing the reported cases to ensure timely and appropriate responses.

**Individual Scope**
The system is feasible as it leverages existing technologies for secure data management and reporting. It addresses a critical need for a safe reporting mechanism within the university environment.

## Features

Secure user authentication
Confidential case reporting
Case management and tracking
Data analysis and reporting

 # Class Implementation

## Domain Classes – University GBV Tracker

## Key Classes
- `User`: Represents a student, counselor, or admin
- `Report`: Represents a GBV case report
- `Case`: Tracks the investigation and status
- `Notification`: Manages communication with stakeholders

## Package Structure
- `/models`: Domain model classes
- `/repositories`: Data layer abstraction
- `/services`: Business logic (optional)
- `/tests`: Test coverage

## Notes
Each domain class is serializable and contains minimal logic to maintain clean separation from services. IDs are used as primary identifiers in the repository layer.

**Unit Testing – GBV Tracker Repository** 

## Focus
Unit tests are designed for `InMemory*Repository` classes to ensure reliable CRUD operations without dependency on external databases.

## Tools
- JUnit 5
- Mockito (optional for services)

## Tested Methods
- `save()`: Adds or updates entries
- `findById()`: Retrieves entries by ID
- `findAll()`: Lists all entries
- `delete()`: Deletes an entry

## Running Tests

```bash
./gradlew test

**Repository Structure**

 ## Features Implemented

| Feature | Description | Justification |
|--------|-------------|---------------|
| **Repository Interface Abstraction** | Defined generic repository interfaces for key entities (e.g., `ReportRepository`, `UserRepository`). | Promotes **code reusability**, **loose coupling**, and easier unit testing. |
| **In-Memory Repository Implementations** | Implemented repositories using `HashMap` for runtime data storage. | Enables **quick development** and **testability** without requiring a database. |
| **Factory Pattern for Storage Selection** | Created `RepositoryFactory` to dynamically instantiate repository types. | **Encapsulates object creation** and allows **extensibility** for future storage backends. |
| **Stub for Future Storage (Database)** | Included placeholder classes for database repositories (e.g., `DatabaseReportRepository`). | **Future-proofs** the system by planning for external storage integration. |
| **Unit Testing for Repository Layer** | Created JUnit tests to verify in-memory CRUD operations. | Ensures **reliability**, **test coverage**, and **early detection** of defects. |

---

## Custom Kanban Board

**Customization Choices**
Added 'Testing' Column: To align with QA requirements and ensure tasks are tested before completion. This column is crucial for verifying the functionality and reliability of features such as GBV case reporting and notification systems.
Added 'Blocked' Column: To identify and address any tasks that are blocked and need attention. This column helps the team quickly identify and resolve issues that may hinder progress, ensuring that critical tasks related to GBV case management are not delayed.
Linked Issues: User stories from Assignment 6 are linked to the board for better traceability. Each issue represents a specific user story, ensuring that tasks are aligned with project requirements and goals.
Task Assignments: Tasks are assigned to team members using @mentions to ensure accountability and clear responsibilities. This approach fosters collaboration and ensures that each team member knows their role and responsibilities.

**Columns**
To Do: Tasks that are yet to be started.
In Progress: Tasks that are currently being worked on.
Testing: Tasks that are under testing to ensure quality and reliability.
Blocked: Tasks that are blocked and need attention to resolve issues.
Done: Completed tasks.

## Changelog

Created Report model using Pydantic for data validation.
Developed InMemoryReportRepository with full CRUD support.
Implemented ReportService for business logic:
**Input validation**
Storage through repository pattern
Built RESTful API endpoints with FastAPI:
POST /api/reports — Create a new report
GET /api/reports — List all reports
GET /api/reports/{id} — Retrieve report by ID
DELETE /api/reports/{id} — Delete a report
Auto-generated API documentation using Swagger UI (/docs).
Included OpenAPI export at /docs/openapi.json.
**Tests**
Added unit tests for ReportService (create, retrieve).
Added integration tests for API endpoints using FastAPI's TestClient.
Fixed
Fixed 500 Internal Server Error when deleting a non-existent report.
Improved error messaging for empty descriptions (400 Bad Request).
Resolved crash on invalid JSON input in POST /api/reports.
**Documentation**
Added API documentation via Swagger (OpenAPI 3.0).
Linked GitHub commits to issues for traceability:
Close #21: Implement report service
Close #22: Add in-memory ReportRepository
Close #23: Expose /api/reports routes
Close #24: Create Report model schema
Close #27: Write unit test for create_report
Kanban board updated with service/API workflow.
**Tags**

feature: Initial API endpoints and services
bug: Critical fix for report deletion error
doc: Swagger/OpenAPI documentation adde
Assignment 12 Implementation

### 1. Service Layer
Implemented service classes for:
- `ReportService`
- `UserService`
- `CaseService`

Each service:
- Uses in-memory repository from Assignment 11
- Validates input and enforces basic rules

### 2. REST API
Developed using **FastAPI**:
- `POST /api/reports` – Create a report
- `GET /api/reports/{id}` – Get report by ID
- `GET /api/reports` – List all reports
- `DELETE /api/reports/{id}` – Delete a report

### 3. Documentation
Swagger UI is auto-generated by FastAPI:
- Visit: `http://localhost:8000/docs`

OpenAPI JSON can be exported to `/docs/openapi.json`

### 4. GitHub Activity
- Issues created for each service & API
- Linked commits with messages like: `Close #5: Implement report API`
- Screenshot uploaded in `/docs/github_board.png`

---

##  Testing

### Unit Tests
Run unit tests:
```bash
pytest tests/test_services.py

##  CI/CD Pipeline

###  How it works
- Every push and PR triggers a GitHub Actions workflow (`.github/workflows/ci.yml`).
- It installs dependencies, runs all unit and API tests using `pytest`.
- If all tests pass and code is merged to `main`, it builds a Python release package (`dist/*.whl`) and uploads it as an artifact.

###  Run Tests Locally
```bash
pip install -r requirements.txt
pytest tests/



