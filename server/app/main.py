from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
import httpx
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app.routers import employee_router
from app.database.connection import engine
from app.database import models

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize scheduler
scheduler = AsyncIOScheduler()


async def keep_alive_ping():
    """Ping the render service to prevent cold start"""
    render_service_url = os.getenv("render_service")
    if not render_service_url:
        logger.warning("render_service URL not configured in environment")
        return
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(render_service_url, timeout=30.0)
            logger.info(f"Keep-alive ping successful: {response.status_code}")
    except Exception as e:
        logger.error(f"Keep-alive ping failed: {str(e)}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan - startup and shutdown events"""
    # Startup: Start the scheduler
    scheduler.add_job(
        keep_alive_ping,
        trigger=IntervalTrigger(minutes=14),
        id="keep_alive_job",
        name="Ping render service every 14 minutes",
        replace_existing=True
    )
    scheduler.start()
    logger.info("Keep-alive scheduler started - pinging every 14 minutes")
    
    yield
    
    # Shutdown: Stop the scheduler
    scheduler.shutdown()
    logger.info("Keep-alive scheduler stopped")


app = FastAPI(
    title="Employee Directory API",
    description="API for searching and managing employee directory",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(employee_router.router, prefix="/api/v1", tags=["employees"])


@app.get("/")
def root():
    return {"message": "Employee Directory API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
