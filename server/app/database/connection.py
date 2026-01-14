from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# Database configuration from environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:password@localhost:3306/employee_directory"
)

# Create SQLAlchemy engine
# pool_pre_ping: Enables connection health checks before using a connection
# pool_recycle: Recycles connections after 3600 seconds to prevent stale connections
# This approach is suitable because:
# 1. Connection pooling improves performance by reusing connections
# 2. Pre-ping ensures we don't use dead connections
# 3. Pool recycling handles MySQL's default 8-hour connection timeout
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False  # Set to True for SQL query logging during development
)

# Session factory for creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()


def get_db():
    """
    Dependency function that provides a database session.
    Ensures proper cleanup of database connections.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
