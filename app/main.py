from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Social Friend Graph API")

app.include_router(router)
