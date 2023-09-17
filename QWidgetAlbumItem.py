from pathlib import Path
import sys
import subprocess

from PySide6.QtCore import QEvent, Signal, Qt
from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QRubberBand,
    QMenu,
    QMessageBox,
    QDialog,
)
from PySide6.QtGui import QCloseEvent, QPixmap, QEnterEvent, QMouseEvent, QCursor

from UI.QWidgetAlbumItem_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, AlbumInfo
from WorkerAlbumItem import WorkerAlbumItem
from QDialogDateTime import QDialogDateTime
from QDialogCover import QDialogCover


class QWidgetAlbumItem(QWidget):
    signal_AlbumItemChanged = Signal(int)

    def __init__(self, albumInfo: AlbumInfo) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerAlbumItem(self.workPath)
        self.worker.start()
        self.albumInfo = albumInfo
        self.pic = QPixmap()
        self.loaded = False
        # UI Init
        self.ui.setupUi(self)
        self.ui.labelDatetime.setText(
            self.albumInfo.shootTime.toString("yyyy-MM-dd HH:mm:ss")
        )
        self.contextMenu = QMenu(self)
        actionOpen = self.contextMenu.addAction("Open with System Method")
        actionLocate = self.contextMenu.addAction("Locate in File Explorer")
        if not albumInfo.isMovie:
            actionCover = self.contextMenu.addAction("Set as Album Cover")
        actionTime = self.contextMenu.addAction("Update Shoot Time")
        actionDelete = self.contextMenu.addAction("Delete")

        self.rubberBand = QRubberBand(QRubberBand.Shape.Rectangle, self.ui.labelPic)
        self.rubberBand.setStyleSheet("background-color: rgba(255, 0, 0, 100);")
        self.rubberBand.hide()
        # UI Singal -> Slot
        actionOpen.triggered.connect(self.ui_actionOpen_triggered)
        actionLocate.triggered.connect(self.ui_actionLocate_triggered)
        if not albumInfo.isMovie:
            actionCover.triggered.connect(self.ui_actionCover_triggered)
        actionTime.triggered.connect(self.ui_actionTime_triggered)
        actionDelete.triggered.connect(self.ui_actionDelete_triggered)

        # Init DiveSite
        self.worker.add(
            func=self.worker.GetDiveSite,
            para=self.albumInfo.shootTime,
            callback=self.callback_GetDiveSite,
            reciever=self,
        )

    def OpenMedia(self):
        platform = sys.platform
        if platform.startswith("win"):
            subprocess.run(
                ["start", "explorer", str(self.albumInfo.albumPath)], shell=True
            )
        elif platform.startswith("darwin"):
            subprocess.run(["open", str(self.albumInfo.albumPath)])
        elif platform.startswith("linux"):
            subprocess.run(["xdg-open", str(self.albumInfo.albumPath)])
        else:
            pass

    def Locate(self):
        platform = sys.platform
        if platform.startswith("win"):
            subprocess.run(["explorer", "/select,", str(self.albumInfo.albumPath)])
        elif platform.startswith("darwin"):
            subprocess.run(["open", "-R", str(self.albumInfo.albumPath)])
        elif platform.startswith("linux"):
            subprocess.run(["xdg-open", str(self.albumInfo.albumPath)])
        else:
            pass

    def load(self):
        if not self.loaded:
            self.loaded = True
            self.worker.add(
                func=self.worker.LoadThumb,
                para=(self.albumInfo.thumbPath, self.albumInfo.isMovie),
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

    def ui_actionOpen_triggered(self):
        self.OpenMedia()

    def ui_actionLocate_triggered(self):
        self.Locate()

    def ui_actionCover_triggered(self):
        qDialogCover = QDialogCover(self.albumInfo.albumPath)
        if qDialogCover.exec() == QDialog.DialogCode.Accepted:
            self.worker.add(
                func=self.worker.ChangeCover,
                para=(self.albumInfo.taxonomicId, qDialogCover.thumb),
                callback=self.callback_ChangeCover,
                reciever=self,
            )
        pass

    def ui_actionTime_triggered(self):
        qDialogDateTime = QDialogDateTime(self.albumInfo.shootTime)
        if qDialogDateTime.exec() == QDialog.DialogCode.Accepted:
            self.worker.add(
                func=self.worker.UpdateTime,
                para=(self.albumInfo.id, qDialogDateTime.datetimeEdit.dateTime()),
                callback=self.callback_UpdateTime,
                reciever=self,
            )

    def ui_actionDelete_triggered(self):
        result = QMessageBox.question(
            self,
            "Warning",
            "Please Confirm Delete Operation",
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Cancel,
        )
        if result != QMessageBox.StandardButton.Ok:
            return
        self.worker.add(
            func=self.worker.DeleteMedia,
            para=self.albumInfo,
            callback=self.callback_DeleteMedia,
            reciever=self,
        )
        pass

    def callback_ChangeCover(self, para):
        QMessageBox.information(self, "Information", "Cover Changed!")
        self.signal_AlbumItemChanged.emit(self.albumInfo.taxonomicId)

    def callback_UpdateTime(self, para):
        QMessageBox.information(self, "Information", "Time Changed!")
        self.signal_AlbumItemChanged.emit(self.albumInfo.taxonomicId)

    def callback_DeleteMedia(self, para):
        QMessageBox.information(self, "Information", "Media Deleted!")
        self.signal_AlbumItemChanged.emit(self.albumInfo.taxonomicId)

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

    def callback_GetDiveSite(self, diveSite: str):
        self.ui.labelDiveSite.setText(diveSite)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            self.contextMenu.exec(QCursor.pos())
        return super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.OpenMedia()
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
