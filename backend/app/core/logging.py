import logging
import json
import traceback
from datetime import datetime
from starlette.requests import Request

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        
        if record.exc_info:
            log_record["exception"] = "".join(traceback.format_exception(*record.exc_info))

        if hasattr(record, "request_info"):
            log_record["request"] = record.request_info
            
        return json.dumps(log_record)

def setup_logging():
    logger = logging.getLogger("aurum")
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    
    # clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.addHandler(handler)
    return logger

logger = setup_logging()
