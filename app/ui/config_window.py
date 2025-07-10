from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QListWidget, QListWidgetItem, QMessageBox
)
from PySide6.QtCore import (Slot, Qt)
from app.ui.widgets.character_form import CharacterForm
from app.ui.edit_character_dialog import EditCharactersDialog
from app.ui.combat_overlay import CombatOverlay

class ConfigWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("D&D Combat Config")
        self.setMinimumSize(800, 600)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.init_character_management_ui()
        self.init_character_selection_ui()
        self.init_combat_button_ui()

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

    def init_character_selection_ui(self):
        group_box = QGroupBox("Select Characters for Combat")
        layout = QVBoxLayout()

        self.character_list = QListWidget()
        self.character_list.setSelectionMode(QListWidget.MultiSelection)
        self.selected_characters = []

        self.load_character_list()

        self.character_list.itemSelectionChanged.connect(self.handle_selection_changed)

        layout.addWidget(self.character_list)
        group_box.setLayout(layout)
        self.main_layout.addWidget(group_box)

    def init_combat_button_ui(self):
        self.open_overlay_button = QPushButton("Iniciar Combate")
        self.open_overlay_button.clicked.connect(self.open_combat_overlay)
        self.main_layout.addWidget(self.open_overlay_button)

    def load_character_list(self):
        self.character_list.clear()
        self.all_characters = self.controller.get_all_characters()
        for char in self.all_characters:
            text = (
                f"{char.name} ({char.type.value})"
                f" - HP: {char.current_hp}/{char.max_hp}, "
                f"CA: {char.ca_def}, FORT: {char.fort_def}, REF: {char.ref_def}, WIL: {char.vol_def}"
            )
            item = QListWidgetItem(text)
            item.setData(1000, char)
            self.character_list.addItem(item)

    def handle_selection_changed(self):
        self.selected_characters = []
        for item in self.character_list.selectedItems():
            char = item.data(1000)
            self.selected_characters.append(char)

    def on_character_created(self):
        self.load_character_list()

    @Slot()
    def open_create_form(self):
        def handle_submit(data):
            self.controller.create_character(data)
            self.on_character_created()
            form.accept()
        form = CharacterForm(on_submit=handle_submit, parent=self)
        form.exec()

    @Slot()
    def open_edit_form(self):
        dialog = EditCharactersDialog(self.controller, self)
        dialog.character_updated.connect(self.load_character_list)
        dialog.exec()

    @Slot()
    def open_combat_overlay(self):
        selected_items = self.character_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Aviso", "Debes seleccionar al menos un personaje.")
            return

        selected_characters = [item.data(1000) for item in selected_items if item.data(1000) is not None]

        overlay = CombatOverlay(self.controller, selected_characters)
        overlay.character_updated.connect(self.load_character_list)
        overlay.exec()
