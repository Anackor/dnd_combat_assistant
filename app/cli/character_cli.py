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
        "folder": args.folder or "Sin carpeta",
    }

    character = service.create(data)
    db.close()
    print(f"✅ Character '{character.name}' created (ID: {character.id}) in folder '{character.folder}'")


def list_characters(args):
    db = SessionLocal()
    service = CharacterService(db)
    characters = service.list_all()
    db.close()

    # Group by folder
    folders = {}
    for char in characters:
        folder = char.folder or "Sin carpeta"
        if folder not in folders:
            folders[folder] = []
        folders[folder].append(char)

    # Print organized by folder
    for folder in sorted(folders.keys()):
        print(f"\n📁 {folder}")
        for char in folders[folder]:
            print(f"  - [{char.id}] {char.name}: {char.current_hp}/{char.max_hp} HP (Type: {char.type.value})")


def move_character(args):
    """Move a character to a different folder"""
    db = SessionLocal()
    service = CharacterService(db)
    
    char = service.get_by_id(args.char_id)
    if not char:
        print(f"❌ Character with ID {args.char_id} not found")
    else:
        old_folder = char.folder
        service.update_character_folder(args.char_id, args.folder)
        print(f"✅ Moved '{char.name}' from '{old_folder}' to '{args.folder}'")
    
    db.close()


def list_folders(args):
    """List all existing folders"""
    db = SessionLocal()
    service = CharacterService(db)
    folders = service.get_folders()
    db.close()
    
    if not folders:
        print("No folders created yet")
    else:
        print("📁 Existing folders:")
        for folder in sorted(folders):
            print(f"  - {folder}")


def duplicate_character(args):
    """Create a copy of a character"""
    db = SessionLocal()
    service = CharacterService(db)
    
    new_char = service.duplicate_character(args.char_id)
    if new_char:
        print(f"✅ Character '{new_char.name}' created successfully!")
    else:
        print(f"❌ Character with ID {args.char_id} not found")
    
    db.close()


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
    create_parser.add_argument("--folder", type=str, required=False, help="Folder to assign character to")
    create_parser.set_defaults(func=create_character)

    list_parser = subparsers.add_parser("list-characters", help="List all characters (grouped by folder)")
    list_parser.set_defaults(func=list_characters)

    move_parser = subparsers.add_parser("move-character", help="Move a character to a different folder")
    move_parser.add_argument("--char-id", type=int, required=True, help="Character ID to move")
    move_parser.add_argument("--folder", type=str, required=True, help="Target folder name")
    move_parser.set_defaults(func=move_character)

    folders_parser = subparsers.add_parser("list-folders", help="List all existing folders")
    folders_parser.set_defaults(func=list_folders)

    duplicate_parser = subparsers.add_parser("duplicate-character", help="Create a copy of a character")
    duplicate_parser.add_argument("--char-id", type=int, required=True, help="Character ID to duplicate")
    duplicate_parser.set_defaults(func=duplicate_character)
