from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

// связь с бд
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
