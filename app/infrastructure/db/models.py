from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    max_hp = Column(Integer, nullable=False)
    current_hp = Column(Integer, nullable=False)
    ca_def = Column(Integer, nullable=False)
    ref_def = Column(Integer, nullable=False)
    fort_def = Column(Integer, nullable=False)
    vol_def = Column(Integer, nullable=False)
