from PySide6.QtWidgets import QTextEdit, QSizePolicy
from PySide6.QtCore import QTimer, Signal

class ExpandingTextEdit(QTextEdit):
    resized = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumHeight(24)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        QTimer.singleShot(0, self.adjustHeight)

        self.textChanged.connect(self.adjustHeight)

    def adjustHeight(self):
        doc_height = self.document().size().height()
        self.setFixedHeight(int(doc_height + 5))
        new_height = int(doc_height + 5)
        if new_height != self.height():
            self.setFixedHeight(new_height)
            self.resized.emit()
