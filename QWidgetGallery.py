from pathlib import Path

from PySide6.QtCore import Signal, Qt, Slot, QSize, QMargins
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QCloseEvent, QResizeEvent

from UI.QWidgetGallery_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicItem
from WorkerGallery import WorkerGallery
from QWidgetGalleryItem import QWidgetGalleryItem


class QWidgetGallery(QWidget):
    signal_ItemSelectionChanged = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerGallery(self.workPath)
        self.worker.start()
        self.itemList: list[QWidgetGalleryItem] = []
        self.itemSize = QSize(300, 330)
        self.itemColCount = 0
        self.waitDynamicLoad = False
        self.idList = []
        # UI Init
        self.ui.setupUi(self)
        self.ui.sliderSize.valueChanged.connect(self.ui_sliderSize_valueChanged)
        self.ui.scrollArea.verticalScrollBar().valueChanged.connect(
            self.ui_scrollArea_verticalScrollBar_valueChanged
        )
        # UI Singal -> Slot

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

    def ui_sliderSize_valueChanged(self, value):
        self.ResizeItem()
        self.ReLocateItem()

    def ui_scrollArea_verticalScrollBar_valueChanged(self, value):
        self.ReLocateItem()

    @Slot(int)
    def slot_AlbumCoverChanged(self, id: int):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_ItemSelectionChanged, self.idList)
        )

    @Slot(list)
    def slot_ItemSelectionChanged(self, idList: list[int]):
        self.idList = idList
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_ItemSelectionChanged, idList)
        )

    def callback_ItemSelectionChanged(self, idList: list[int]):
        self.worker.add(
            func=self.worker.GetTaxonomicItemList,
            para=idList,
            callback=self.callback_GetTaxonomicItemList,
            reciever=self,
        )
        pass

    @Slot(TaxonomicItem)
    def slot_MouseDoubleClicked(self, taxonomicItem: TaxonomicItem):
        self.signal_ItemSelectionChanged.emit(taxonomicItem.id)
        pass

    def callback_GetTaxonomicItemList(self, taxonomicItemList: list[TaxonomicItem]):
        for item in self.itemList:
            item.closeEvent(QCloseEvent())
            item.signal_MouseDoubleClicked.disconnect(self.slot_MouseDoubleClicked)
            item.deleteLater()
        self.itemList.clear()
        for taxonomicItem in taxonomicItemList:
            item = QWidgetGalleryItem(taxonomicItem)
            item.signal_MouseDoubleClicked.connect(self.slot_MouseDoubleClicked)
            self.itemList.append(item)
        self.ui.labelAlbumNumber.setText(f"{str(len(taxonomicItemList))} Albums")
        self.ResizeItem()
        self.ReLocateItem()

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
