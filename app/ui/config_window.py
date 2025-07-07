import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def run_app():
    app = QApplication(sys.argv)

    window = ConfigWindow()
    window.show()

    sys.exit(app.exec())

class ConfigWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D&D Combat Assistant - Config")
        self.setMinimumSize(400, 300)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Configuration Window - Placeholder")
        layout.addWidget(label)

        self.setLayout(layout)
