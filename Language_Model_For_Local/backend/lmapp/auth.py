from fastapi import Request, HTTPException, Depends
from fastapi.security import APIKeyHeader
from typing import Optional
from core.config import settings  # Import settings from config

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def verify_api_key(api_key: Optional[str] = Depends(api_key_header)) -> str:
    if api_key == settings.API_KEY:
        return api_key
    raise HTTPException(status_code=403, detail="Invalid API Key")
