from fastapi import APIRouter, HTTPException
from typing import List
from models.report import Report
from repositories.report_repository import InMemoryReportRepository
from services.report_service import ReportService

router = APIRouter()
report_service = ReportService(InMemoryReportRepository())

@router.post("/api/reports", response_model=Report, tags=["Reports"])
def create_report(report: Report):
    try:
        report_service.create_report(report)
        return report
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/reports/{report_id}", response_model=Report, tags=["Reports"])
def get_report(report_id: str):
    report = report_service.get_report(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.get("/api/reports", response_model=List[Report], tags=["Reports"])
def list_reports():
    return report_service.get_all_reports()

@router.delete("/api/reports/{report_id}", tags=["Reports"])
def delete_report(report_id: str):
    report_service.delete_report(report_id)
    return {"message": "Report deleted successfully"}
