from fastapi import APIRouter

from app.api.api_v1.handlers.speech_to_text import speech_to_text_router


app_router = APIRouter()


app_router.include_router(speech_to_text_router, prefix="/ws")