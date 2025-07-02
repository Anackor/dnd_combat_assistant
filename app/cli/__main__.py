import argparse
from app.cli.character_cli import register_character_commands

def main():
    parser = argparse.ArgumentParser(description="D&D Assistant CLI")
    subparsers = parser.add_subparsers(title="Commands")

    # Registrar los comandos específicos
    register_character_commands(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
