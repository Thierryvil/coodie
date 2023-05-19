from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from src.db.config import engine
from src.routes.job_routes import router as job_router
from src.routes.login_routes import router as login_router

app = FastAPI()
app.include_router(job_router)
app.include_router(login_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLModel.metadata.create_all(engine)
