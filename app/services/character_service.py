from sqlalchemy.orm import Session
from app.infrastructure.db.models.character import Character

class CharacterService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Character:
        character = Character(**data)
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character

    def update(self, character):
        self.db.commit()

    def list_all(self) -> list[Character]:
        return self.db.query(Character).all()

    def get_by_id(self, char_id: int) -> Character | None:
        return self.db.query(Character).filter_by(id=char_id).first()

    def delete(self, char_id: int) -> bool:
        char = self.get_by_id(char_id)
        if char:
            self.db.delete(char)
            self.db.commit()
            return True
        return False
