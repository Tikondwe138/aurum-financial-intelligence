from fastapi import APIRouter
from app.services.insight_engine import generate_insights

router = APIRouter()

@router.get("/")
def insights():
    return {"insights": generate_insights()}
