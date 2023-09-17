import sys
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QPushButton,
    QDateTimeEdit,
)
from PySide6.QtCore import QDateTime


class QDialogDateTime(QDialog):
    def __init__(self, datetime: QDateTime):
        self.datetime = datetime
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.datetimeEdit = QDateTimeEdit(self)
        self.datetimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.datetimeEdit.setDateTime(self.datetime)
        layout.addWidget(self.datetimeEdit)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        self.setWindowTitle("Fix Datetime")
