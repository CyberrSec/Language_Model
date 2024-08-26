from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from lmapp.models.language_model import LanguageModelService
from lmapp.auth import verify_api_key

router = APIRouter()
service = LanguageModelService()


def api_key_header(api_key: str = Header(...)):
    if api_key != "your_actual_api_key_here":
        raise HTTPException(status_code=403, detail="Invalid API Key")

class TextRequest(BaseModel):
    text: str

@router.post("/summarize")
async def summarize_text(request: TextRequest, api_key: str = Depends(verify_api_key)):
    try:
        summary = service.summarize_text(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/analyze-sentiment")
async def analyze_sentiment(request: TextRequest, api_key: str = Depends(verify_api_key)):
    try:
        sentiment = service.analyze_sentiment(request.text)
        return sentiment
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
