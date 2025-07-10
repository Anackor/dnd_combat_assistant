from sqlalchemy import Column, Integer, String, Enum
from app.infrastructure.db.database import Base
from sqlalchemy import Column, Integer, String
from app.infrastructure.db.models.enums import CharacterType

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
    type = Column(Enum(CharacterType), nullable=False, default=CharacterType.NPC)
