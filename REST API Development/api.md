from fastapi import APIRouter, HTTPException
from models.report import Report
from services.report_service import ReportService
from repositories.report_repository import InMemoryReportRepository

router = APIRouter()
report_service = ReportService(InMemoryReportRepository())

@router.post("/api/reports", response_model=Report)
def create_report(report: Report):
    try:
        report_service.create_report(report)
        return report
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/api/reports/{report_id}", response_model=Report)
def get_report(report_id: str):
    report = report_service.get_report(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.get("/api/reports", response_model=list[Report])
def list_reports():
    return report_service.get_all_reports()

@router.delete("/api/reports/{report_id}")
def delete_report(report_id: str):
    report_service.delete_report(report_id)
    return {"message": "Report deleted"}
    
