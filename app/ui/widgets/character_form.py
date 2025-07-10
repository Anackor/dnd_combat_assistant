from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit,
    QSpinBox, QComboBox, QPushButton, QMessageBox
)
from app.infrastructure.db.models.enums import CharacterType

class CharacterForm(QDialog):
    def __init__(self, on_submit, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Character")
        self.on_submit = on_submit

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.max_hp_input = QSpinBox()
        self.max_hp_input.setRange(0, 999)

        self.current_hp_input = QSpinBox()
        self.current_hp_input.setRange(0, 999)

        self.ca_def_input = QSpinBox()
        self.ca_def_input.setRange(0, 999)

        self.ref_def_input = QSpinBox()
        self.ref_def_input.setRange(0, 999)

        self.fort_def_input = QSpinBox()
        self.fort_def_input.setRange(0, 999)

        self.vol_def_input = QSpinBox()
        self.vol_def_input.setRange(0, 999)

        self.type_input = QComboBox()
        self.type_input.addItems([e.value for e in CharacterType])

        self.form_layout.addRow("Name", self.name_input)
        self.form_layout.addRow("Max HP", self.max_hp_input)
        self.form_layout.addRow("Current HP", self.current_hp_input)
        self.form_layout.addRow("CA", self.ca_def_input)
        self.form_layout.addRow("REF", self.ref_def_input)
        self.form_layout.addRow("FORT", self.fort_def_input)
        self.form_layout.addRow("VOL", self.vol_def_input)
        self.form_layout.addRow("Type", self.type_input)

        self.layout.addLayout(self.form_layout)

        self.submit_button = QPushButton("Create")
        self.submit_button.clicked.connect(self.submit)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def submit(self):
        name = self.name_input.text()
        if not name:
            QMessageBox.warning(self, "Missing Field", "Name is required.")
            return

        data = {
            "name": name,
            "max_hp": self.max_hp_input.value(),
            "current_hp": self.current_hp_input.value(),
            "ca_def": self.ca_def_input.value(),
            "ref_def": self.ref_def_input.value(),
            "fort_def": self.fort_def_input.value(),
            "vol_def": self.vol_def_input.value(),
            "type": self.type_input.currentText(),
        }

        self.on_submit(data)

    def set_data(self, character):
        # Name
        self.name_input.setText(character.name if character.name else "")

        # Max HP
        self.set_spinbox_value(self.max_hp_input, character.max_hp)

        # Current HP
        self.set_spinbox_value(self.current_hp_input, character.current_hp)

        # Defensas
        self.set_spinbox_value(self.ca_def_input, character.ca_def)
        self.set_spinbox_value(self.ref_def_input, character.ref_def)
        self.set_spinbox_value(self.fort_def_input, character.fort_def)
        self.set_spinbox_value(self.vol_def_input, character.vol_def)

        # Tipo
        index = self.type_input.findText(character.type.value if character.type else "")
        if index != -1:
            self.type_input.setCurrentIndex(index)
        else:
            self.type_input.setCurrentIndex(-1)

    def set_spinbox_value(self, spinbox, value):
        if value is not None:
            spinbox.setValue(value)
        else:
            spinbox.clear()

    def clear(self):
        self.name_input.clear()
        self.max_hp_input.clear()
        self.current_hp_input.clear()
        self.ca_def_input.clear()
        self.ref_def_input.clear()
        self.fort_def_input.clear()
        self.vol_def_input.clear()
        self.type_input.setCurrentIndex(-1)
