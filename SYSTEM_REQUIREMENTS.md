# System Requirements

## Functional Requirements

1. The system shall allow students to report GBV cases confidentially.
   - Acceptance Criteria: Reports must be encrypted and accessible only to authorized personnel.
2. The system shall provide a user-friendly interface for reporting cases.
   -Acceptance Criteria: Users should be able to complete the reporting process within 5 minutes.
3. The system shall allow clinic staff to manage and track reported cases.
   -Acceptance Criteria: Staff should be able to update case status and add notes.
4. The system shall generate compliance and usage reports for university administrators.
   -Acceptance Criteria: Reports must include compliance metrics and system usage statistics, generated monthly.
5. The system shall provide data analysis tools for data analysts.
   -Acceptance Criteria: Analysts should be able to generate accurate reports within 2 minutes.
6. The system shall ensure data security and confidentiality.
   -Acceptance Criteria: All data must be encrypted using AES-256.
7. The system shall support user authentication.
   -Acceptance Criteria: Users must log in using their university credentials.
8. The system shall allow counselors to access case details.
   -Acceptance Criteria: Counselors should be able to view case details within 1 minute of logging in.
9. The system shall provide notifications to clinic staff for new cases.
   -Acceptance Criteria: Staff should receive notifications within 1 minute of a new case being reported.
10. The system shall allow administrators to configure system settings.
    -Acceptance Criteria: Administrators should be able to update settings without system downtime.
11. The system shall notify the University Security Department of GBV incidents.
    -Acceptance Criteria: Security personnel should receive notifications within 1 minute of a new case being reported.
12. The system shall allow the University Security Department to access relevant case details.
    -Acceptance Criteria: Security personnel should be able to view case details necessary for their response within 1 minute of logging in.
13. The system shall enable coordination between clinic staff and the University Security Department.
    -Acceptance Criteria: Both parties should be able to add notes and updates to cases to facilitate coordination.
14. The system shall provide instant notifications to students about the status of their reports.
    -Acceptance Criteria: Students should receive notifications within 1 minute of any status change.

## Non-Functional Requirements

1. Usability: The interface shall comply with WCAG 2.1 accessibility standards.
   - Rationale: Ensures the system is accessible to all users, including those with disabilities.
2. Deployability: The system shall be deployable on Windows and Linux servers.
   - Rationale: Provides flexibility in deployment environments.
3. Maintainability: Documentation shall include an API guide for future integrations.
   - Rationale: Facilitates future development and integration with other systems.
4. Scalability: Support 1,000 concurrent users during peak hours.
   - Rationale: Ensures the system can handle high usage without performance degradation.
5. Security: All user data shall be encrypted using AES-256.
   - Rationale: Protects sensitive information from unauthorized access.
6. Performance: Search results shall load within 2 seconds.
   - Rationale: Provides a responsive user experience.
7. Reliability: The system shall have an uptime of 99.9%.
   - **Rationale: Ensures the system is available when needed.
8. Compliance: The system shall comply with relevant data protection regulations.
   - Rationale: Ensures legal and regulatory adherence.
