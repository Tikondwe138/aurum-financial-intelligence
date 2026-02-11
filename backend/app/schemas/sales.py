from pydantic import BaseModel
from datetime import date

class SaleSchema(BaseModel):
    revenue: float
    date: date
