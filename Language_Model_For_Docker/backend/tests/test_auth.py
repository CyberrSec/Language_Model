
from fastapi.testclient import TestClient
from lmapp.main import app
from lmapp.core.config import settings

client = TestClient(app)

def test_no_api_key():
    response = client.post("/lmapi/v1/summarize", json={"text": "test"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid API Key"}

def test_invalid_api_key():
    headers = {"X-API-KEY": "invalid-key"}
    response = client.post("/lmapi/v1/summarize", headers=headers, json={"text": "test"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid API Key"}

def test_valid_api_key():
    headers = {"X-API-KEY": settings.API_KEY}
    response = client.post("/lmapi/v1/summarize", headers=headers, json={"text": "test"})
    # Check if it proceeds to further checks after API key is accepted
    assert response.status_code in [200, 500]  # 500 because no valid input model is not part of this test
