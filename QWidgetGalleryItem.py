from pathlib import Path

from PySide6.QtCore import QEvent, Signal
from PySide6.QtWidgets import QWidget, QApplication, QRubberBand
from PySide6.QtGui import (
    QCloseEvent,
    QPixmap,
    QEnterEvent,
    QMouseEvent,
)

from UI.QWidgetGalleryItem_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicItem
from WorkerGalleryItem import WorkerGalleryItem


class QWidgetGalleryItem(QWidget):
    signal_MouseDoubleClicked = Signal(TaxonomicItem)

    def __init__(self, taxonomicItem: TaxonomicItem = TaxonomicItem()) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerGalleryItem(self.workPath)
        self.worker.start()
        self.taxonomicItem = taxonomicItem
        self.path = self.workPath.joinpath(f"img/thumb/{self.taxonomicItem.name}.jpg")
        self.pic = QPixmap()
        self.loaded = False
        # UI Init
        self.ui.setupUi(self)
        self.ui.labelCommonName.setText(self.taxonomicItem.commonName)
        self.ui.labelName.setText(self.taxonomicItem.name)
        self.rubberBand = QRubberBand(QRubberBand.Shape.Rectangle, self.ui.labelPic)
        self.rubberBand.setStyleSheet("background-color: rgba(255, 0, 0, 100);")
        self.rubberBand.hide()
        # UI Singal -> Slot

    def load(self):
        if not self.loaded:
            self.loaded = True
            self.worker.add(
                func=self.worker.LoadThumb,
                para=self.path,
                callback=self.callback_LoadThumb,
                reciever=self,
            )
        else:
            self.worker.add(
                func=self.worker.DisplayThumb,
                para=(self.pic, self.ui.labelPic.size()),
                callback=self.callback_DisplayThumb,
                reciever=self,
                changeCursor=False,
            )

    def callback_LoadThumb(self, pic: QPixmap):
        self.pic = pic
        self.worker.add(
            func=self.worker.DisplayThumb,
            para=(self.pic, self.ui.labelPic.size()),
            callback=self.callback_DisplayThumb,
            reciever=self,
            changeCursor=False,
        )

    def callback_DisplayThumb(self, pic: QPixmap):
        self.ui.labelPic.setPixmap(pic)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.signal_MouseDoubleClicked.emit(self.taxonomicItem)
        return super().mouseDoubleClickEvent(event)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.rubberBand.setGeometry(self.ui.labelPic.rect())
        self.rubberBand.show()
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.rubberBand.hide()
        return super().leaveEvent(event)

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        return super().closeEvent(event)
