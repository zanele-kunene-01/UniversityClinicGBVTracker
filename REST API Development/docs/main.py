from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="University GBV Tracker API",
    description="API for reporting and tracking Gender-Based Violence (GBV) incidents.",
    version="1.0.0"
)

app.include_router(router)
