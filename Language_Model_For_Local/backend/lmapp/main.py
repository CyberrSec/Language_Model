from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import endpoints
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="This is a language model API with endpoints for text summarization and sentiment analysis.",
    version="1.0.0",
    contact={
        "name": "Kshitij Tapale",
        "email": "kshitijtaple@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)
# Configure CORS with dynamic origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.ALLOWED_ORIGINS.split(',')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints.router, prefix=settings.API_V1_STR)
