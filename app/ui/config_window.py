from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
)
from PySide6.QtCore import Slot

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
        self.btn_delete = QPushButton("Delete Character")

        self.btn_create.clicked.connect(self.open_create_form)
        self.btn_edit.clicked.connect(self.open_edit_form)
        self.btn_delete.clicked.connect(self.delete_selected_character)

        layout.addWidget(self.btn_create)
        layout.addWidget(self.btn_edit)
        layout.addWidget(self.btn_delete)

        group_box.setLayout(layout)
        self.main_layout.addWidget(group_box)

    @Slot()
    def open_create_form(self):
        print("TODO: Abrir formulario de creación de personaje")

    @Slot()
    def open_edit_form(self):
        print("TODO: Abrir formulario de edición de personaje")

    @Slot()
    def delete_selected_character(self):
        print("TODO: Eliminar personaje seleccionado")
