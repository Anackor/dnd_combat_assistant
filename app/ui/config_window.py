from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTreeWidget, 
    QTreeWidgetItem, QMessageBox, QInputDialog, QSpinBox, QDialog
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
        self.active_overlay = None

    def init_character_management_ui(self):
        group_box = QGroupBox("Character Management")
        layout = QHBoxLayout()

        self.btn_create = QPushButton("Create Character")
        self.btn_edit = QPushButton("Edit Character")
        self.btn_new_folder = QPushButton("New Folder")
        self.btn_add_copies = QPushButton("Add Copies to Combat")

        self.btn_create.clicked.connect(self.open_create_form)
        self.btn_edit.clicked.connect(self.open_edit_form)
        self.btn_new_folder.clicked.connect(self.create_new_folder)
        self.btn_add_copies.clicked.connect(self.add_multiple_copies)

        layout.addWidget(self.btn_create)
        layout.addWidget(self.btn_edit)
        layout.addWidget(self.btn_new_folder)
        layout.addWidget(self.btn_add_copies)

        group_box.setLayout(layout)
        self.main_layout.addWidget(group_box)

    def init_character_selection_ui(self):
        group_box = QGroupBox("Select Characters for Combat")
        layout = QVBoxLayout()

        self.character_tree = QTreeWidget()
        self.character_tree.setHeaderLabels(["Character"])
        self.character_tree.setSelectionMode(QTreeWidget.MultiSelection)
        self.character_tree.itemSelectionChanged.connect(self.handle_selection_changed)

        self.load_character_tree()

        layout.addWidget(self.character_tree)
        group_box.setLayout(layout)
        self.main_layout.addWidget(group_box)

    def init_combat_button_ui(self):
        self.open_overlay_button = QPushButton("Iniciar Combate")
        self.open_overlay_button.clicked.connect(self.open_combat_overlay)
        self.main_layout.addWidget(self.open_overlay_button)

    def load_character_tree(self):
        """Load characters organized by folders into tree widget"""
        self.character_tree.clear()
        self.all_characters = self.controller.get_all_characters()
        
        # Group characters by folder
        folders = {}
        for char in self.all_characters:
            folder = char.folder or "Sin carpeta"
            if folder not in folders:
                folders[folder] = []
            folders[folder].append(char)
        
        # Populate tree
        for folder_name in sorted(folders.keys()):
            folder_item = QTreeWidgetItem([folder_name])
            folder_item.setData(0, 1000, None)  # Mark as folder
            
            for char in folders[folder_name]:
                text = (
                    f"{char.name} ({char.type.value})"
                    f" - HP: {char.current_hp}/{char.max_hp}, "
                    f"CA: {char.ca_def}, FORT: {char.fort_def}, REF: {char.ref_def}, VOL: {char.vol_def}"
                )
                char_item = QTreeWidgetItem([text])
                char_item.setData(0, 1000, char)
                folder_item.addChild(char_item)
            
            self.character_tree.addTopLevelItem(folder_item)
            folder_item.setExpanded(True)

    def handle_selection_changed(self):
        """Extract selected characters from tree"""
        self.selected_characters = []
        for item in self.character_tree.selectedItems():
            char = item.data(0, 1000)
            if char is not None:  # Only add if it's a character, not a folder
                self.selected_characters.append(char)

    def on_character_created(self):
        self.load_character_tree()

    def create_new_folder(self):
        """Create a new folder by opening character creation with folder pre-selected"""
        folder_name, ok = QInputDialog.getText(
            self, 
            "New Folder", 
            "Enter folder name:"
        )
        if ok and folder_name:
            # Open create form with this folder pre-selected
            def handle_submit(data):
                self.controller.create_character(data)
                self.on_character_created()
                form.accept()
            form = CharacterForm(on_submit=handle_submit, parent=self)
            form.folder_input.setEditText(folder_name)
            form.exec()

    def add_multiple_copies(self):
        """Add multiple copies of selected character to combat"""
        selected_items = self.character_tree.selectedItems()
        
        # Filter to get only actual characters (not folders)
        selected_chars = [item.data(0, 1000) for item in selected_items if item.data(0, 1000) is not None]
        
        if len(selected_chars) != 1:
            QMessageBox.warning(
                self, 
                "Selection Required", 
                "Please select exactly ONE character to add multiple copies."
            )
            return
        
        char = selected_chars[0]
        
        # Ask how many copies
        count, ok = QInputDialog.getInt(
            self,
            "Add Copies",
            f"How many copies of '{char.name}' to add?",
            2, 1, 20, 1
        )
        
        if ok:
            # Add the same character multiple times to selection
            for _ in range(count - 1):  # -1 because it's already selected
                self.selected_characters.append(char)
            
            QMessageBox.information(
                self,
                "Success",
                f"Added {count} copies of '{char.name}' to combat selection."
            )

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
        dialog.character_updated.connect(self.load_character_tree)
        dialog.exec()

    @Slot()
    def open_combat_overlay(self):
        if not self.selected_characters:
            QMessageBox.warning(self, "Aviso", "Debes seleccionar al menos un personaje.")
            return

        if self.active_overlay and self.active_overlay.isVisible():
            self.active_overlay.raise_()
            self.active_overlay.activateWindow()
            return

        overlay = CombatOverlay(self.controller, self.selected_characters)
        overlay.character_updated.connect(self.load_character_tree)
        overlay.finished.connect(lambda _: setattr(self, 'active_overlay', None))
        self.active_overlay = overlay
        overlay.show()
        overlay.raise_()
        overlay.activateWindow()
