# Contributing to University Clinic GBV Tracker

Thank you for wanting to help! This guide explains how to get the project,
tests and CI running locally, our coding conventions, and the pull-request
workflow.

---

## 1. Prerequisites
| Tool | Version | Purpose |
|------|---------|---------|
| Python | ≥ 3.11 | main runtime |
| Poetry **or** pip | latest | dependency management |
| Git | ≥ 2.30 | VCS |
| Make (optional) | | handy shortcuts |

```bash
# clone
git clone https://github.com/zanele-kunene-01/UniversityClinicGBVTracker.git
cd UniversityClinicGBVTracker
# install dependencies
pip install -r requirements.txt   # or: poetry install
# run tests
pytest
# run the API
uvicorn main:app --reload
