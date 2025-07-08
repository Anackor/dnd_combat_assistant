import argparse
from app.cli.character_cli import register_character_commands

def main():
    parser = argparse.ArgumentParser(prog="dnd-combat-assistant")
    subparsers = parser.add_subparsers(dest="command")

    register_character_commands(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
