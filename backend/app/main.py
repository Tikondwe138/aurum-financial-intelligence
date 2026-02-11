from fastapi import FastAPI
from app.api.v1 import health, kpis, forecasts, insights

app = FastAPI(
    title="Aurum Financial Intelligence API",
    description="SME Decision Intelligence Platform",
    version="1.0.0"
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(kpis.router, prefix="/api/v1")
app.include_router(forecasts.router, prefix="/api/v1")
app.include_router(insights.router, prefix="/api/v1")
