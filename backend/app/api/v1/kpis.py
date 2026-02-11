from fastapi import APIRouter
from app.services.kpi_engine import calculate_profit_margin

router = APIRouter()

@router.get("/")
def get_kpis():
    sample_data = [
        {"revenue": 10000, "cost": 6500},
        {"revenue": 8000, "cost": 5000}
    ]
    margin = calculate_profit_margin(sample_data)
    return {"profit_margin": margin}
