from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Coordinates Storage Service B"
)

app.include_router(router)
