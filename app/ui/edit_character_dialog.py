from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton
from PySide6.QtCore import Signal
from app.ui.widgets.character_form import CharacterForm

class EditCharactersDialog(QDialog):
    character_updated = Signal()

    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.selected_character = None
        self.setWindowTitle("Editar personajes")
        self.setMinimumSize(600, 400)

        # Widgets
        self.list_widget = QListWidget()
        self.character_form = CharacterForm(on_submit=self.save_changes)
        self.character_form.setDisabled(True)
        self.delete_button = QPushButton("Eliminar")
        self.delete_button.setVisible(False)

        # Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.delete_button)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.character_form)
        right_layout.addLayout(button_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.list_widget, 2)
        main_layout.addLayout(right_layout, 3)

        self.setLayout(main_layout)

        # Events
        self.list_widget.itemClicked.connect(self.load_character)
        self.delete_button.clicked.connect(self.delete_character)

        self.load_characters()

    def load_characters(self):
        self.list_widget.clear()
        self.characters = self.controller.get_all_characters()
        for char in self.characters:
            self.list_widget.addItem(f"{char.name} ({char.type})")

    def load_character(self, item):
        index = self.list_widget.row(item)
        self.selected_character = self.characters[index]
        self.character_form.setDisabled(False)
        self.character_form.set_data(self.selected_character)
        self.delete_button.setVisible(True)

    def save_changes(self, data):
        if self.selected_character:
            for k, v in data.items():
                setattr(self.selected_character, k, v)
            self.controller.update_character(self.selected_character)
            self.load_characters()
            self.character_updated.emit() 

    def delete_character(self):
        if self.selected_character:
            self.controller.delete_character(self.selected_character.id)
            self.selected_character = None
            self.character_form.clear()
            self.character_form.setDisabled(True)
            self.delete_button.setVisible(False)
            self.load_characters()
            self.character_updated.emit()
