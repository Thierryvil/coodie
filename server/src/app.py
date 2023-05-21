from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from src.db.config import engine
from src.routes.auth_routes import router as auth_router
from src.routes.enterprise_routes import router as enterprise_router

app = FastAPI()
app.include_router(enterprise_router)
app.include_router(auth_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLModel.metadata.create_all(engine)
