from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def forecast_stub():
    return {
        "forecast": [
            {"month": "2026-01", "value": 12000},
            {"month": "2026-02", "value": 13500}
        ]
    }
