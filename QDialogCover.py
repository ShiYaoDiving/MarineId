import sys
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QApplication,
    QMessageBox,
    QRubberBand,
)
from PySide6.QtCore import QDateTime, Signal, Qt, QSize, QRect
from pathlib import Path


class QDialogCover(QDialog):
    def __init__(self, path: Path):
        self.path = path
        super().__init__()
        self.pic = QPixmap()
        self.picSize = QSize()
        self.preview = QPixmap()
        self.thumb = QPixmap()
        self.previewRect = QRect()
        self.picRect = QRect()
        self.ratio = 1

        self.initUI()

    def MakeThumb(self):
        rect = QRect(
            int(self.previewRect.left() * self.ratio),
            int(self.previewRect.top() * self.ratio),
            int(self.previewRect.width() * self.ratio),
            int(self.previewRect.height() * self.ratio),
        )
        thumb = self.pic.copy(rect)
        thumb = thumb.scaled(
            QSize(600, 600),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation,
        )
        thumb = thumb.copy(
            (thumb.size().width() - 600) / 2,
            (thumb.size().height() - 600) / 2,
            600,
            600,
        )
        self.thumb = thumb

    def initUI(self):
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        QApplication.processEvents()
        self.pic = QPixmap(self.path)
        self.picSize = self.pic.size()
        self.preview = self.pic.scaled(
            QSize(600, 600), Qt.AspectRatioMode.KeepAspectRatioByExpanding
        )
        self.previewSize = self.preview.size()
        self.previewRect = self.preview.rect()
        self.ratio = self.picSize.width() / self.previewSize.width()
        self.MakeThumb()
        QApplication.restoreOverrideCursor()
        if not self.pic:
            QMessageBox.warning(self, "Warning", "Media Not Found")
        else:
            layoutMain = QHBoxLayout()
            layoutSub = QVBoxLayout()

            self.labelPic = QLabel(self)
            self.labelPic.setFixedSize(self.previewSize)
            self.labelPic.setPixmap(self.preview)
            self.labelPic.mousePressEvent = self.labelPic_mousePressEvent
            self.labelPic.mouseMoveEvent = self.labelPic_mouseMoveEvent
            self.labelPic.mouseReleaseEvent = self.labelPic_mouseReleaseEvent
            self.rubberBand = QRubberBand(QRubberBand.Shape.Rectangle, self.labelPic)
            self.labelThumb = QLabel(self)
            self.labelThumb.setFixedSize(QSize(150, 150))
            self.labelThumb.setScaledContents(True)
            self.labelThumb.setPixmap(self.thumb)
            self.labelNull = QLabel(self)
            self.pushButtonOK = QPushButton("OK", self)
            self.pushButtonOK.clicked.connect(self.accept)
            self.pushButtonCANCEL = QPushButton("CANCEL", self)
            self.pushButtonCANCEL.clicked.connect(self.reject)
            layoutSub.addWidget(self.labelThumb)
            layoutSub.addWidget(self.labelNull)
            layoutSub.addWidget(self.pushButtonOK)
            layoutSub.addWidget(self.pushButtonCANCEL)
            layoutMain.addWidget(self.labelPic)
            layoutMain.addLayout(layoutSub)
            self.setLayout(layoutMain)
            self.setWindowTitle("Set Cover")

    def labelPic_mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.startPos = event.position().toPoint()
            self.rubberBand.setGeometry(QRect(self.startPos, QSize()))
            self.rubberBand.show()
        pass

    def labelPic_mouseMoveEvent(self, event: QMouseEvent):
        if self.startPos:
            endPos = event.position().toPoint()
            w = endPos.x() - self.startPos.x()
            h = endPos.y() - self.startPos.y()
            l = max(abs(w), abs(h))
            if endPos.x() > self.startPos.x():
                endPos.setX(self.startPos.x() + l)
            else:
                endPos.setX(self.startPos.x() - l)
            if endPos.y() > self.startPos.y():
                endPos.setY(self.startPos.y() + l)
            else:
                endPos.setY(self.startPos.y() - l)

            self.rubberBand.setGeometry(QRect(self.startPos, endPos).normalized())
        pass

    def labelPic_mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.rubberBand.hide()
            self.previewRect = self.rubberBand.geometry()
            self.MakeThumb()
            self.labelThumb.setPixmap(self.thumb)
