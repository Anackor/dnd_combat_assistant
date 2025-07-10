from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import (Qt, Signal)

class CombatOverlay(QDialog):
    character_updated = Signal()

    def __init__(self, controller, characters, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Combat Overlay")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
        self.characters = characters
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        for char in self.characters:
            layout.addWidget(self.create_character_card(char))

    def create_character_card(self, char):
        card = QWidget()
        card.setObjectName("characterCard")

        card.setStyleSheet("""
            QWidget#characterCard {
                border: 1px solid #aaa;
                border-radius: 4px;
            }
            QLabel {
                font-size: 11px;
            }
            QLineEdit {
                font-size: 11px;
                max-width: 40px;
            }
        """)

        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(6, 4, 6, 4)

        # Nombre con color según tipo
        name_label = QLabel(f"<b>{char.name}</b>")
        name_label.setStyleSheet(
            "color: #2ecc71;" if char.type.value == "PJ" else "color: #e74c3c;"
        )
        layout.addWidget(name_label)

        # HP: current / max
        layout.addWidget(QLabel("HP:"))

        current_hp_input = QLineEdit(str(char.current_hp))
        current_hp_input.setFixedWidth(40)
        current_hp_input.editingFinished.connect(
            lambda: self.update_hp(char, current_hp_input)
        )
        layout.addWidget(current_hp_input)

        layout.addWidget(QLabel(f"/ {char.max_hp}"))

        # Defensas en orden: CA, FORT, REF, VOL
        for label, value in [("CA", char.ca_def), ("FORT", char.fort_def),
                            ("REF", char.ref_def), ("VOL", char.vol_def)]:
            layout.addWidget(QLabel(f"{label}:"))

            defense_input = QLineEdit(str(value))
            defense_input.setFixedWidth(25)
            layout.addWidget(defense_input)

        card.setLayout(layout)
        return card

    def update_hp(self, char, hp_input):
        text = hp_input.text()
        try:
            new_hp = int(eval(text, {"__builtins__": {}}))
            char.current_hp = new_hp
            self.controller.update_character(char)
            hp_input.setText(str(new_hp))
            self.character_updated.emit()
        except Exception:
            hp_input.setText(str(char.current_hp))
