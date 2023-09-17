from pathlib import Path

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QWidget, QMessageBox, QTreeWidgetItem, QApplication
from PySide6.QtGui import QCloseEvent

from UI.QWidgetTree_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicItem, TaxonomicTree
from WorkerTree import WorkerTree
from Worker import WorkerTask


class QWidgetTree(QWidget):
    signal_ItemSelectionChanged = Signal(list)

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerTree(self.workPath)
        self.worker.start()
        self.treeWidgetItemDict: dict[int, QTreeWidgetItem] = {}
        self.orphanTreeWidgetItem = QTreeWidgetItem()
        self.idToSelect = 0
        # UI Init
        self.ui.setupUi(self)
        # UI Singal -> Slot
        self.ui.treeWidgetTaxonomic.itemSelectionChanged.connect(
            self.ui_treeWidgetTaxonomic_itemSelectionChanged
        )
        # Init Tree
        self.worker.add(
            func=self.worker.GetTaxonomicTree,
            para=None,
            callback=self.callback_GetTaxonomicTree,
            reciever=self,
        )

    def SelectIdList(self, IdList: list[int]):
        for id in IdList:
            item = self.treeWidgetItemDict.get(id, self.orphanTreeWidgetItem)
            self.ui.treeWidgetTaxonomic.setCurrentItem(item)
            item.setExpanded(True)
            item.setSelected(True)

    @Slot(int)
    def slot_DbTaxonomicChanged(self, id: int):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_DbTaxonomicChanged, id)
        )

    def callback_DbTaxonomicChanged(self, id: int):
        self.idToSelect = id
        self.worker.add(
            func=self.worker.GetTaxonomicTree,
            para=None,
            callback=self.callback_GetTaxonomicTree,
            reciever=self,
        )

    @Slot(list)
    def slot_SearchResultSelected(self, idList: list[int]):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_SearchResultSelected, idList)
        )

    @Slot(int)
    def slot_GalleryItemSelected(self, id):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_GalleryItemSelected, id)
        )

    def callback_GalleryItemSelected(self, id):
        item = self.treeWidgetItemDict.get(id, self.orphanTreeWidgetItem)
        self.ui.treeWidgetTaxonomic.setCurrentItem(item)
        item.setExpanded(True)
        item.setSelected(True)

    def callback_SearchResultSelected(self, idList: list[int]):
        self.SelectIdList(idList)

    def callback_GetTaxonomicTree(self, taxonomicTree: TaxonomicTree):
        self.taxonomicTree = taxonomicTree
        self.ui.treeWidgetTaxonomic.clear()
        self.treeWidgetItemDict.clear()
        for taxonomicItem in taxonomicTree.itemDict.values():
            treeWidgetItem = QTreeWidgetItem()
            treeWidgetItem.setData(
                0,
                Qt.ItemDataRole.DisplayRole,
                f"[{taxonomicItem.commonName}] {taxonomicItem.name}",
            )
            treeWidgetItem.setData(0, Qt.ItemDataRole.UserRole, taxonomicItem)
            self.treeWidgetItemDict[taxonomicItem.id] = treeWidgetItem
            if taxonomicItem.parentId == 0:
                self.ui.treeWidgetTaxonomic.addTopLevelItem(treeWidgetItem)
            if taxonomicItem.rank == "Orphan":
                self.orphanTreeWidgetItem = treeWidgetItem
        for id, treeWidgetItem in self.treeWidgetItemDict.items():
            taxonomicItem: TaxonomicItem = treeWidgetItem.data(
                0, Qt.ItemDataRole.UserRole
            )
            if taxonomicItem.parentId != 0:
                try:
                    self.treeWidgetItemDict[taxonomicItem.parentId].addChild(
                        treeWidgetItem
                    )
                except:
                    self.orphanTreeWidgetItem.addChild(treeWidgetItem)
        self.SelectIdList([self.idToSelect])
        pass

    def ui_treeWidgetTaxonomic_itemSelectionChanged(self):
        treeWidgetItemList = self.ui.treeWidgetTaxonomic.selectedItems()
        idList = [
            treeWidgetItem.data(0, Qt.ItemDataRole.UserRole).id
            for treeWidgetItem in treeWidgetItemList
        ]
        self.signal_ItemSelectionChanged.emit(idList)

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        return super().closeEvent(event)
