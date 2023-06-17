from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.config import create_puc, create_tables
from routes.auth_routes import router as auth_router
from routes.job_routes import router as job_routes
from routes.user_router import router as user_router

app = FastAPI()
app.include_router(job_routes)
app.include_router(auth_router)
app.include_router(user_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()
create_puc()
