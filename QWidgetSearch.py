from pathlib import Path

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem, QApplication
from PySide6.QtGui import QCloseEvent

from UI.QWidgetSearch_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicItem
from WorkerSearch import WorkerSearch


class QWidgetSearch(QWidget):
    signal_SearchResultSelected = Signal(list)

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerSearch(self.workPath)
        self.worker.start()
        # UI Init
        self.ui.setupUi(self)
        # UI Singal -> Slot
        self.ui.lineEditKeyword.textChanged.connect(self.ui_lineEditKeyword_textChanged)
        self.ui.pushButtonSearch.clicked.connect(self.ui_pushButtonSearch_clicked)
        self.ui.listWidgetResult.itemSelectionChanged.connect(
            self.ui_listWidgetResult_itemSelectionChanged
        )

    def callback_SearchTaxonomic(self, taxonomicItemList: list[TaxonomicItem]):
        self.ui.listWidgetResult.clear()
        for taxonomicItem in taxonomicItemList:
            displayString = f"{taxonomicItem.rank}:[{taxonomicItem.commonName}] {taxonomicItem.name}"
            listWidgetItem = QListWidgetItem()
            listWidgetItem.setData(Qt.ItemDataRole.UserRole, taxonomicItem)
            listWidgetItem.setData(Qt.ItemDataRole.DisplayRole, displayString)
            self.ui.listWidgetResult.addItem(listWidgetItem)

    def ui_pushButtonSearch_clicked(self):
        self.worker.add(
            func=self.worker.SearchTaxonomic,
            para=self.ui.lineEditKeyword.text().strip(),
            callback=self.callback_SearchTaxonomic,
            reciever=self,
        )

    def ui_lineEditKeyword_textChanged(self, text):
        self.ui.pushButtonSearch.setEnabled(text.strip() != "")

    def ui_listWidgetResult_itemSelectionChanged(self):
        listWidgetItemList = self.ui.listWidgetResult.selectedItems()
        idList = list()
        for listWidgetItem in listWidgetItemList:
            taxonomicItem: TaxonomicItem = listWidgetItem.data(Qt.ItemDataRole.UserRole)
            idList.append(taxonomicItem.id)
        self.signal_SearchResultSelected.emit(idList)

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        return super().closeEvent(event)
