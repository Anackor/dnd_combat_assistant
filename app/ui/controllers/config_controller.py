from app.services.character_service import CharacterService

class ConfigController:
    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self):
        return self.character_service.list_characters()

    def create_character(self, name, max_hp, current_hp, ca, ref, fort, vol, char_type):
        return self.character_service.create_character(
            name=name,
            max_hp=max_hp,
            current_hp=current_hp,
            ca_def=ca,
            ref_def=ref,
            fort_def=fort,
            vol_def=vol,
            char_type=char_type
        )
