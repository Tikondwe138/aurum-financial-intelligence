from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks, HTTPException
from typing import List, Dict, Any
from app.api.deps import get_current_tenant, require_role
from app.models.tenants import Tenant
from app.models.users import UserRole
from app.services.etl_service import process_sales_upload
import json

router = APIRouter()

@router.post("/upload/sales")
def upload_sales_data(
    file: UploadFile = File(...),
    tenant: Tenant = Depends(get_current_tenant),
    _=Depends(require_role([UserRole.ADMIN, UserRole.ANALYST]))
):
    """
    Endpoint for uploading raw sales data in JSON format for the specific tenant.
    Triggers a background Celery task for parsing, validation, and insertion.
    """
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="Only JSON files are supported for uploads.")
    
    try:
        content = file.file.read()
        data: List[Dict[str, Any]] = json.loads(content)
        
        # Trigger Celery background task
        task = process_sales_upload.delay(data, tenant.id)
        
        return {"message": "Sales data ingestion started.", "task_id": task.id}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file format.")
    finally:
        file.file.close()

@router.get("/task/{task_id}")
def get_task_status(
    task_id: str,
    _: Tenant = Depends(get_current_tenant)
):
    """Check the status of a background ETL task."""
    from app.core.celery_app import celery_app
    task_result = celery_app.AsyncResult(task_id)
    
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result if task_result.ready() else None
    }
    
    # If the task supports progress metadata
    if task_result.state == 'PROGRESS':
        result["progress"] = task_result.info
        
    return result
