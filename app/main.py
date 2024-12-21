from fastapi import FastAPI

from app.api.api_v1.router import app_router

app = FastAPI()

app.include_router(router=app_router)
