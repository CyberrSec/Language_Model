from lmapp.core.config import settings

def test_settings_loads_correctly():
    assert settings.PROJECT_NAME == "Language Model API"
    assert settings.API_V1_STR == "/lmapi/v1"
    # The API_KEY should be the value in your environment or "default-secret-api-key"
    assert settings.API_KEY == "default-secret-api-key"
