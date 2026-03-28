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

    def get_folders(self) -> list[str]:
        """Get all unique folders"""
        folders = self.db.query(Character.folder).distinct().all()
        return sorted([f[0] for f in folders if f[0]])

    def get_by_folder(self, folder: str) -> list[Character]:
        """Get all characters in a specific folder"""
        return self.db.query(Character).filter_by(folder=folder).all()

    def update_character_folder(self, char_id: int, folder: str):
        """Move a character to a different folder"""
        char = self.get_by_id(char_id)
        if char:
            char.folder = folder
            self.db.commit()

    def duplicate_character(self, char_id: int) -> Character | None:
        """Create a copy of a character with (Copy) suffix"""
        original = self.get_by_id(char_id)
        if not original:
            return None
        
        # Create new character with same attributes
        duplicate = Character(
            name=f"{original.name} (Copy)",
            max_hp=original.max_hp,
            current_hp=original.current_hp,
            ca_def=original.ca_def,
            ref_def=original.ref_def,
            fort_def=original.fort_def,
            vol_def=original.vol_def,
            type=original.type,
            folder=original.folder,
        )
        self.db.add(duplicate)
        self.db.commit()
        self.db.refresh(duplicate)
        return duplicate
