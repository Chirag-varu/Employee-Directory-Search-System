from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routers import employee_router
from app.database.connection import engine
from app.database import models

# Load environment variables
load_dotenv()

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Directory API",
    description="API for searching and managing employee directory",
    version="1.0.0"
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(employee_router.router, prefix="/api", tags=["employees"])


@app.get("/")
def root():
    return {"message": "Employee Directory API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
