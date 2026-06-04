from fastapi import FastAPI

from api.upload import router as upload_router
from api.query import router as query_router

app = FastAPI(
    title="Enterprise Agentic AI"
)

app.include_router(upload_router)

app.include_router(query_router)