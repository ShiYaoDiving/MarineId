from pathlib import Path

from PySide6.QtCore import Signal, Qt, Slot, QSize
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from PySide6.QtGui import QCloseEvent, QResizeEvent, QDragEnterEvent, QDropEvent

from UI.QWidgetAlbum_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicItem, AlbumData, AlbumInfo
from WorkerAlbum import WorkerAlbum
from QWidgetAlbumItem import QWidgetAlbumItem
from PySide6.QtGui import QPixmap


class QWidgetAlbum(QWidget):
    signal_AlbumCoverChanged = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerAlbum(self.workPath)
        self.worker.start()
        self.itemList: list[QWidgetAlbumItem] = []
        self.itemSize = QSize(300, 330)
        self.itemColCount = 0
        self.waitDynamicLoad = False
        self.albumData = AlbumData(TaxonomicItem(), QPixmap(), [])

        # UI Init
        self.ui.setupUi(self)
        # UI Singal -> Slot
        self.ui.sliderSize.valueChanged.connect(self.ui_sliderSize_valueChanged)
        self.ui.scrollArea.verticalScrollBar().valueChanged.connect(
            self.ui_scrollArea_verticalScrollBar_valueChanged
        )

    def ResizeItem(self):
        self.itemSize = QSize(
            self.ui.sliderSize.value(), self.ui.sliderSize.value() + 30
        )
        for item in self.itemList:
            item.setFixedSize(self.itemSize)
        self.itemColCount = 0

    def ReLocateItem(self):
        scrollValue = self.ui.scrollArea.verticalScrollBar().value()
        viewHeight = self.ui.scrollArea.viewport().rect().height()
        viewWidth = self.ui.scrollArea.viewport().rect().width()
        viewTopMargin = self.ui.gridLayout.contentsMargins().top()
        itemHeight = self.itemSize.height()
        itemWidth = self.itemSize.width()
        itemColCount = int(viewWidth / itemWidth)
        itemColCount = itemColCount if itemColCount != 0 else 1
        viewTop = scrollValue + viewTopMargin
        startRow = int(viewTop / itemHeight)
        endRow = int((viewTop + viewHeight) / itemHeight) + 1

        if self.itemColCount != itemColCount:
            self.itemColCount = itemColCount
            for i, item in enumerate(self.itemList):
                self.ui.gridLayout.addWidget(
                    item,
                    int(i / self.itemColCount),
                    i % self.itemColCount,
                    Qt.AlignmentFlag.AlignCenter,
                )

        indexStart = startRow * itemColCount
        indexEnd = endRow * itemColCount
        for item in self.itemList[indexStart:indexEnd]:
            item.load()

    @Slot(int)
    def slot_AlbumItemChanged(self, id: int):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_ItemSelectionChanged, id)
        )
        self.signal_AlbumCoverChanged.emit(id)

    @Slot(int)
    def slot_ItemSelectionChanged(self, id: int):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_ItemSelectionChanged, id)
        )

    def callback_ItemSelectionChanged(self, id: int):
        self.worker.add(
            func=self.worker.GetAlbumData,
            para=id,
            callback=self.callback_GetAlbumData,
            reciever=self,
        )

    def callback_GetAlbumData(self, albumData: AlbumData):
        self.albumData = albumData
        self.ui.labelName.setText(self.albumData.taxonomicItem.name)
        self.ui.labelCommon.setText(self.albumData.taxonomicItem.commonName)
        self.ui.labelOther.setText(self.albumData.taxonomicItem.otherNames)
        self.ui.plainTextEditInfomation.setPlainText(
            self.albumData.taxonomicItem.information
        )
        self.ui.labelThumb.setPixmap(self.albumData.thumbPic)
        for item in self.itemList:
            item.closeEvent(QCloseEvent())
            item.signal_AlbumItemChanged.disconnect(self.slot_AlbumItemChanged)
            item.deleteLater()
        self.itemList.clear()
        for albumInfo in self.albumData.albumInfoList:
            item = QWidgetAlbumItem(albumInfo)
            item.signal_AlbumItemChanged.connect(self.slot_AlbumItemChanged)
            self.itemList.append(item)
        self.ResizeItem()
        self.ReLocateItem()

    def callback_AddMedia(self, count: int):
        QMessageBox.information(self, "Information", f"{count} Media(s) Added")
        self.worker.add(
            func=self.worker.GetAlbumData,
            para=self.albumData.taxonomicItem.id,
            callback=self.callback_GetAlbumData,
            reciever=self,
        )
        pass

    def ui_sliderSize_valueChanged(self, value):
        self.ResizeItem()
        self.ReLocateItem()

    def ui_scrollArea_verticalScrollBar_valueChanged(self, value):
        self.ReLocateItem()

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.acceptProposedAction()
        return super().dragEnterEvent(event)

    def dropEvent(self, event: QDropEvent) -> None:
        urls = event.mimeData().urls()
        pathList = [Path(url.toLocalFile()) for url in urls]
        self.worker.add(
            func=self.worker.AddMedia,
            para=(self.albumData, pathList),
            callback=self.callback_AddMedia,
            reciever=self,
        )
        return super().dropEvent(event)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.ReLocateItem()
        return super().resizeEvent(event)

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        for item in self.itemList:
            item.closeEvent(event)
        return super().closeEvent(event)
