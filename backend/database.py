from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Connection string for SQLite (local DB file)
DATABASE_URL = "sqlite:///./moodplanner.db"

# Create engine (connects to DB)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# DB sessions (for reading/writing)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for all DB models
Base = declarative_base()
