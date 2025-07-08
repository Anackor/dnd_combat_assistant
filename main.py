import sys
from PySide6.QtWidgets import QApplication
from app.ui.config_window import ConfigWindow
from app.ui.controllers.config_controller import ConfigController

def run_app():
    app = QApplication(sys.argv)
    controller = ConfigController()
    window = ConfigWindow(controller)
    window.show()
    sys.exit(app.exec_())

def main():
    if len(sys.argv) > 1:
        # Ejecutar CLI
        from app.cli.cli_entrypoint import main as cli_main
        cli_main()
    else:
        # Ejecutar GUI
        run_app()

if __name__ == "__main__":
    main()
