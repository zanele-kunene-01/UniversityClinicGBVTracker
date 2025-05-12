from typing import List, Optional
from models.report import Report

class ReportRepository:
    def save(self, report: Report) -> None:
        raise NotImplementedError

    def find_by_id(self, report_id: str) -> Optional[Report]:
        raise NotImplementedError

    def find_all(self) -> List[Report]:
        raise NotImplementedError

    def delete(self, report_id: str) -> None:
        raise NotImplementedError

class InMemoryReportRepository(ReportRepository):
    def __init__(self):
        self._storage = {}

    def save(self, report: Report) -> None:
        self._storage[report.id] = report

    def find_by_id(self, report_id: str) -> Optional[Report]:
        return self._storage.get(report_id)

    def find_all(self) -> List[Report]:
        return list(self._storage.values())

    def delete(self, report_id: str) -> None:
        if report_id in self._storage:
            del self._storage[report_id]
