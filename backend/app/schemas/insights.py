from pydantic import BaseModel
from typing import List

class InsightResponse(BaseModel):
    insights: List[str]
