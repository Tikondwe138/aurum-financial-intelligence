import pandas as pd
from typing import List, Dict, Any
from app.core.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.sales import Sale
from app.models.expenses import Expense
from app.models.products import Product
from app.schemas.etl import ETLSaleData, ETLExpenseData, ETLProductData
from app.core.logging import logger
from pydantic import ValidationError
import time

@celery_app.task(bind=True, max_retries=3)
def process_sales_upload(self, data: List[Dict[str, Any]], tenant_id: int):
    """Processes an uploaded list of sales dicts, validates them, and inserts into DB."""
    db = SessionLocal()
    try:
        self.update_state(state='PROGRESS', meta={'current': 0, 'total': len(data)})
        
        valid_sales = []
        errors = []
        for index, item in enumerate(data):
            try:
                # Validation
                validated = ETLSaleData(**item)
                sale_model = Sale(
                    revenue=validated.revenue,
                    date=validated.date,
                    tenant_id=tenant_id
                )
                valid_sales.append(sale_model)
            except ValidationError as e:
                errors.append({"row": index, "error": str(e)})
                logger.warning(f"ETL Validation Error (Sales) for Tenant {tenant_id}: {e}")

        if valid_sales:
            db.bulk_save_objects(valid_sales)
            db.commit()
            
        return {"processed": len(valid_sales), "errors": len(errors), "error_details": errors}
    except Exception as exc:
        db.rollback()
        logger.error(f"ETL Sales Pipeline failed: {exc}")
        self.retry(exc=exc, countdown=2 ** self.request.retries)
    finally:
        db.close()

@celery_app.task(bind=True)
def generate_daily_summary(self):
    """Scheduled task to aggregate data across tenants."""
    logger.info("Running daily financial summary aggregation...")
    # This would contain the logic that queries the DB using SQLAlchemy grouping
    # and generates insights or materialized views.
    return {"status": "summary generated"}
