# Use Case Specifications

## Use Case: Report GBV Case
**Actor**: Student  
**Description**: Allows students to report GBV incidents confidentially.  
**Preconditions**: Student must be logged in.  
**Postconditions**: The report is saved and encrypted in the system.  
**Basic Flow**:
1. Student logs into the system.
2. Student navigates to the report GBV case section.
3. Student fills out the report form with incident details.
4. Student submits the report.
**Alternative Flows**:
- If the report form is incomplete, prompt the student to fill in the missing details.

## Use Case: Manage GBV Cases
**Actor**: Clinic Staff  
**Description**: Allows clinic staff to manage and track reported GBV cases.  
**Preconditions**: Clinic staff must be logged in.  
**Postconditions**: Case status and notes are updated in the system.  
**Basic Flow**:
1. Clinic staff logs into the system.
2. Clinic staff views the list of reported cases.
3. Clinic staff updates case status and adds notes.
**Alternative Flows**:
- If the case status update fails, retry or notify IT staff.

## Use Case: Generate Reports
**Actor**: University Admin  
**Description**: Allows university administrators to generate compliance and usage reports.  
**Preconditions**: University admin must be logged in.  
**Postconditions**: The report is generated and available for download.  
**Basic Flow**:
1. University admin logs into the system.
2. University admin navigates to the reports section.
3. University admin selects the type of report to generate.
4. University admin generates the report.
**Alternative Flows**:
- If report generation fails, retry or notify IT staff.

## Use Case: Analyze Data
**Actor**: Data Analyst  
**Description**: Allows data analysts to analyze case data and generate insights.  
**Preconditions**: Data analyst must be logged in.  
**Postconditions**: Insights and reports are generated.  
**Basic Flow**:
1. Data analyst logs into the system.
2. Data analyst navigates to the data analysis section.
3. Data analyst selects the data to analyze.
4. Data analyst generates insights and reports.
**Alternative Flows**:
- If data analysis fails, retry or notify IT staff.

## Use Case: Access Case Details
**Actor**: Counselor  
**Description**: Allows counselors to access detailed information about reported cases.  
**Preconditions**: Counselor must be logged in.  
**Postconditions**: Case details are displayed.  
**Basic Flow**:
1. Counselor logs into the system.
2. Counselor views the list of cases.
3. Counselor selects a case to view details.
**Alternative Flows**:
- If case details retrieval fails, retry or notify IT staff.

## Use Case: Receive Notifications
**Actor**: Clinic Staff, Security Personnel  
**Description**: Sends notifications to clinic staff and security personnel about new cases and updates.  
**Preconditions**: None.  
**Postconditions**: Notifications are sent.  
**Basic Flow**:
1. A new case is reported or an existing case is updated.
2. The system sends notifications to relevant stakeholders.
**Alternative Flows**:
- If notification sending fails, retry or notify IT staff.

## Use Case: Configure System Settings
**Actor**: University Admin  
**Description**: Allows university administrators to configure system settings.  
**Preconditions**: University admin must be logged in.  
**Postconditions**: System settings are updated.  
**Basic Flow**:
1. University admin logs into the system.
2. University admin navigates to the settings section.
3. University admin updates system settings.
**Alternative Flows**:
- If system settings update fails, retry or notify IT staff.

## Use Case: Authenticate Users
**Actor**: IT Staff  
**Description**: Manages user authentication and access control.  
**Preconditions**: IT staff must be logged in.  
**Postconditions**: User accounts and permissions are updated.  
**Basic Flow**:
1. IT staff logs into the system.
2. IT staff manages user accounts and access permissions.
**Alternative Flows**:
- If authentication management fails, retry or notify IT staff.

## Use Case: Coordinate with Security
**Actor**: Clinic Staff, Security Personnel  
**Description**: Facilitates coordination between clinic staff and security personnel for incident management.  
**Preconditions**: Clinic staff and security personnel must be logged in.  
**Postconditions**: Coordination notes and actions are updated.  
**Basic Flow**:
1. Clinic staff and security personnel log into the system.
2. They view and update case details.
3. They add notes and coordinate actions.
**Alternative Flows**:
- If coordination fails, retry or notify IT staff.
