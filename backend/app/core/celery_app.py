from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "aurum_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["app.services.etl_service"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_reject_on_worker_lost=True,
)

# Optional: Celery Beat schedule for repeating tasks
celery_app.conf.beat_schedule = {
    "daily-financial-summary": {
        "task": "app.services.etl_service.generate_daily_summary",
        "schedule": 86400.0, # Every 24 hours (could use crontab here)
    },
}
