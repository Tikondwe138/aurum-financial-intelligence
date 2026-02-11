from pydantic import BaseModel

class KPISchema(BaseModel):
    profit_margin: float
