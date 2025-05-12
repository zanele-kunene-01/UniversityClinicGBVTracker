from pydantic import BaseModel

class Report(BaseModel):
    id: str
    description: str
