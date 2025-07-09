from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
)
from PySide6.QtCore import Slot
from app.ui.widgets.character_form import CharacterForm
from app.ui.edit_character_dialog import EditCharactersDialog

class ConfigWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("D&D Combat Config")
        self.setMinimumSize(800, 600)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.init_character_management_ui()

    def init_character_management_ui(self):
        group_box = QGroupBox("Character Management")
        layout = QHBoxLayout()

        self.btn_create = QPushButton("Create Character")
        self.btn_edit = QPushButton("Edit Character")

        self.btn_create.clicked.connect(self.open_create_form)
        self.btn_edit.clicked.connect(self.open_edit_form)

        layout.addWidget(self.btn_create)
        layout.addWidget(self.btn_edit)

        group_box.setLayout(layout)
        self.main_layout.addWidget(group_box)

    @Slot()
    def open_create_form(self):
        def handle_submit(data):
            self.controller.create_character(data)
            print(f"Character created: {data['name']}")
            form.accept()
        form = CharacterForm(on_submit=handle_submit, parent=self)
        form.exec()

    @Slot()
    def open_edit_form(self):
        dialog = EditCharactersDialog(self.controller, self)
        dialog.exec()
