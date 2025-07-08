import argparse
from app.services.character_service import CharacterService
from app.infrastructure.db.database import SessionLocal


def create_character(args):
    db = SessionLocal()
    service = CharacterService(db)

    data = {
        "name": args.name,
        "max_hp": args.max_hp,
        "current_hp": args.current_hp,
        "ca_def": args.ca_def,
        "ref_def": args.ref_def,
        "fort_def": args.fort_def,
        "vol_def": args.vol_def,
        "type": args.char_type,
    }

    character = service.create(data)
    db.close()
    print(f"✅ Character '{character.name}' created (ID: {character.id})")


def list_characters(args):
    db = SessionLocal()
    service = CharacterService(db)
    characters = service.list_all()
    db.close()

    for char in characters:
        print(f"- [{char.id}] {char.name}: {char.current_hp}/{char.max_hp} HP")


def register_character_commands(subparsers: argparse._SubParsersAction):
    create_parser = subparsers.add_parser("create-character", help="Create a new character")
    create_parser.add_argument("--name", required=True)
    create_parser.add_argument("--max-hp", type=int, required=True)
    create_parser.add_argument("--current-hp", type=int, required=True)
    create_parser.add_argument("--ca-def", type=int, required=True)
    create_parser.add_argument("--ref-def", type=int, required=True)
    create_parser.add_argument("--fort-def", type=int, required=True)
    create_parser.add_argument("--vol-def", type=int, required=True)
    create_parser.add_argument("--char-type", type=str, required=True)
    create_parser.set_defaults(func=create_character)

    list_parser = subparsers.add_parser("list-characters", help="List all characters")
    list_parser.set_defaults(func=list_characters)
