from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1 import health, kpis, forecasts, insights, auth, etl
from app.core.logging import logger

app = FastAPI(
    title="Aurum Financial Intelligence API",
    description="SME Decision Intelligence Platform",
    version="1.0.0"
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled exception", exc_info=exc, extra={"request_info": {"url": str(request.url), "method": request.method}})
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

app.include_router(health.router, prefix="/api/v1")
app.include_router(kpis.router, prefix="/api/v1")
app.include_router(forecasts.router, prefix="/api/v1")
app.include_router(insights.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(etl.router, prefix="/api/v1/etl", tags=["ETL Pipeline"])
