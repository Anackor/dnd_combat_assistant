import sys

def main():
    if len(sys.argv) > 1:
        # Ejecutar CLI
        from app.cli.cli_entrypoint import main as cli_main
        cli_main()
    else:
        # Ejecutar GUI
        from app.ui.config_window import run_app
        run_app()

if __name__ == "__main__":
    main()
