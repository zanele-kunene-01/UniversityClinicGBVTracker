# UniversityClinicGBVTracker
This project aims to develop a system for tracking gender-based violence (GBV) cases reported by students at a university clinic. The system will provide a secure and confidential platform for reporting, managing, and analyzing GBV cases.
The University Clinic GBV Tracker is a secure and confidential platform designed to help students report gender-based violence (GBV) incidents. The system will enable students to report cases safely, allow clinic staff to manage and track these cases efficiently, and provide tools for data analysis to identify trends and generate reports. Key components include a web application for user interaction, a database for storing case and user information, an authentication service for secure access, and API services for data handling. The system will ensure data security and privacy, complying with relevant regulations to protect sensitive information.

https://github.com/zanele-kunene-01/UniversityClinicGBVTracker/blob/main/SPECIFICATION.md SPECIFICATION.md

https://github.com/zanele-kunene-01/UniversityClinicGBVTracker/blob/main/ARCHITECTURE.md ARCHITECTURE.md


 **Class Implementation**

# Domain Classes – University GBV Tracker

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
