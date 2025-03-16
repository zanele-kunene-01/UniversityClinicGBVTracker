# Test Cases

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|--------------|----------------|-------------|-------|-----------------|---------------|--------------------|
| TC001        | FR-001         | Student reports a GBV case | 1. Log in 2. Navigate to report section 3. Fill out form 4. Submit report | Report is saved and encrypted | ... | ... |
| TC002        | FR-002         | Clinic staff manages GBV cases | 1. Log in 2. View cases 3. Update status 4. Add notes | Case status and notes updated | ... | ... |
| TC003        | FR-003         | University admin generates reports | 1. Log in 2. Navigate to reports section 3. Select report type 4. Generate report | Report is generated and available for download | ... | ... |
| TC004        | FR-004         | Data analyst analyzes case data | 1. Log in 2. Navigate to data analysis section 3. Select data to analyze 4. Generate insights | Insights and reports are generated | ... | ... |
| TC005        | FR-005         | Counselor accesses case details | 1. Log in 2. View list of cases 3. Select case to view details | Case details are displayed | ... | ... |
| TC006        | FR-006         | System sends notifications | 1. Report a new case or update an existing case 2. System sends notifications | Notifications are sent to relevant stakeholders | ... | ... |
| TC007        | FR-007         | University admin configures system settings | 1. Log in 2. Navigate to settings section 3. Update system settings | System settings are updated | ... | ... |
| TC008        | FR-008         | IT staff manages user authentication | 1. Log in 2. Manage user accounts and permissions | User accounts and permissions are updated | ... | ... |
| TC009        | FR-009         | Clinic staff coordinates with security | 1. Log in 2. View and update case details 3. Add notes and coordinate actions | Coordination notes and actions are updated | ... | ... |

## Non-Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|--------------|----------------|-------------|-------|-----------------|---------------|--------------------|
| TC010        | NFR-001        | Performance Test: Simulate 1,000 concurrent users | 1. Simulate 1,000 concurrent users 2. Perform searches and report cases | Response time ≤ 2 seconds | ... | ... |
| TC011        | NFR-002        | Security Test: Verify data encryption | 1. Report a GBV case 2. Check data encryption | Data is encrypted using AES-256 | ... | ... |
