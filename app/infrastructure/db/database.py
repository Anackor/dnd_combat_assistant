from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.db.models import Base

DATABASE_URL = "sqlite:///dnd_data.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
