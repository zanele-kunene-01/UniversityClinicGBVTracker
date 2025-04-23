# src/gbv_case.py

class GBVCase:

    def __init__(self, case_id, status, reported_date, resolved_date=None):
        self._case_id = case_id
        self._status = status
        self._reported_date = reported_date
        self._resolved_date = resolved_date


    def assign_case(self):
        self._status = "UnderReview"


    def review_case(self):
        self._status = "Reviewed"


    def escalate_case(self):
        self._status = "Escalated"


    def resolve_case(self):
        self._status = "Resolved"
        self._resolved_date = datetime.now()


    # Getters and setters for attributes

    @property

    def case_id(self):
        return self._case_id


    @property

    def status(self):
        return self._status


    @property

    def reported_date(self):
        return self._reported_date


    @property

    def resolved_date(self):
        return self._resolved_date

# University Clinic GBV Tracker

## Language Choice

I chose Python for implementing the University Clinic GBV Tracker system due to its simplicity, readability, and extensive support for object-oriented programming. Python's rich set of libraries and frameworks also facilitate rapid development and testing, making it an ideal choice for this project.

## Key Design Decisions

### Class Implementation

- **Encapsulation**: Attributes are defined as private fields with getters and setters to ensure data integrity and encapsulation.

- **Methods**: Core functions such as `assign_case()`, `review_case()`, `escalate_case()`, and `resolve_case()` are implemented to manage the lifecycle of a GBV case.

- **Relationships**: Associations between classes are represented through method interactions and attribute references.

        
