
from fastapi.testclient import TestClient
from lmapp.main import app
from lmapp.core.config import settings

client = TestClient(app)

headers = {"X-API-KEY": settings.API_KEY}

def test_summarize_text_valid():
    response = client.post("/lmapi/v1/summarize", headers=headers, json={"text": "This is a test text."})
    assert response.status_code == 200
    assert "summary" in response.json()

def test_summarize_text_invalid():
    response = client.post("/lmapi/v1/summarize", headers=headers, json={"text": ""})
    assert response.status_code == 200  # If input is too short, should return text itself
    assert response.json() == {"summary": ""}

def test_analyze_sentiment_valid():
    response = client.post("/lmapi/v1/analyze-sentiment", headers=headers, json={"text": "This is a test text."})
    assert response.status_code == 200
    assert "overall" in response.json()

def test_analyze_sentiment_invalid():
    response = client.post("/lmapi/v1/analyze-sentiment", headers=headers, json={"text": ""})
    assert response.status_code == 200  # If input is too short, should handle it gracefully
    assert "overall" in response.json()
