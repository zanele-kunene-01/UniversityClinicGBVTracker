UniversityClinicGBVTracker/
├── api/                    # REST API endpoints
│   └── routes.py
├── docs/                   # API documentation (OpenAPI)
├── models/                 # Domain models
│   └── report.py
│   └── user.py
│   └── case.py
├── repositories/           # Repository interfaces and in-memory implementations
│   └── report_repository.py
│   └── user_repository.py
│   └── case_repository.py
├── services/               # Service layer with business logic
│   └── report_service.py
│   └── user_service.py
│   └── case_service.py
├── tests/                  # Unit and integration tests
│   └── test_services.py
│   └── test_api.py
├── main.py                 # FastAPI app entry point
├── requirements.txt
└── README.md               # Project documentation
