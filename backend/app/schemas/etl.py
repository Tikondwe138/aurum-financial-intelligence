from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional

class ETLSaleData(BaseModel):
    revenue: float = Field(..., gt=0)
    date: date
    
    @field_validator("date", mode="before")
    def parse_date(cls, v):
        # Additional custom parsing logic could go here
        return v

class ETLExpenseData(BaseModel):
    category: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    date: date

class ETLProductData(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
