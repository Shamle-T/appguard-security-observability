from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Main database connection manager
engine = create_engine(settings.database_url, pool_pre_ping=True)

# Creates a temporary session with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
