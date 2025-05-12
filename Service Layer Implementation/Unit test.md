from repositories.report_repository import ReportRepository
from models.report import Report

class ReportService:
    def __init__(self, repo: ReportRepository):
        self.repo = repo

    def create_report(self, report: Report):
        if not report.description:
            raise ValueError("Description is required")
        self.repo.save(report)

    def get_report(self, report_id: str):
        return self.repo.find_by_id(report_id)

    def get_all_reports(self):
        return self.repo.find_all()

    def delete_report(self, report_id: str):
        self.repo.delete(report_id)
