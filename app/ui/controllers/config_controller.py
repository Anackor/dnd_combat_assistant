from app.services.character_service import CharacterService
from app.infrastructure.db.database import SessionLocal

class ConfigController:
    def __init__(self):
        db = SessionLocal()
        self.character_service = CharacterService(db)

    def get_all_characters(self):
        return self.character_service.list_all()

    def create_character(self, data: dict):
        return self.character_service.create(data)

    def update_character(self, character):
        self.character_service.update(character)

    def delete_character(self, character_id):
        self.character_service.delete(character_id)