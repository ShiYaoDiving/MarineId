from pathlib import Path

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from PySide6.QtGui import QCloseEvent

from UI.QWidgetUpdate_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicItem
from WorkerUpdate import WorkerUpdate


class QWidgetUpdate(QWidget):
    signal_DBTaxonomicChanged = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerUpdate(self.workPath)
        self.worker.start()
        # UI Init
        self.ui.setupUi(self)
        # UI Singal -> Slot
        self.ui.pushButtonDelete.clicked.connect(self.ui_pushButtonDelete_clicked)
        self.ui.pushButtonUpdate.clicked.connect(self.ui_pushButtonUpdate_clicked)
        self.ui.pushButtonAquaml.clicked.connect(self.ui_pushButtonAquaml_clicked)
        self.ui.pushButtonTaiEOL.clicked.connect(self.ui_pushButtonTaiEOL_clicked)

    @Slot(list)
    def slot_ItemSelectionChanged(self, idList: list[int]):
        QApplication.instance().postEvent(
            self, CallbackEvent(self.callback_ItemSelectionChanged, idList)
        )

    def callback_ItemSelectionChanged(self, idList: list[int]):
        if idList:
            id = idList[0]
            self.worker.add(
                func=self.worker.GetTaxonomicItem,
                para=id,
                callback=self.callback_GetTaxonomicItem,
                reciever=self,
            )
        else:
            QApplication.instance().postEvent(
                self, CallbackEvent(self.callback_GetTaxonomicItem, TaxonomicItem())
            )
            pass

    def callback_GetTaxonomicItem(self, taxonomicItem: TaxonomicItem):
        self.ui.spinBoxId.setValue(taxonomicItem.id)
        self.ui.lineEditRank.setText(taxonomicItem.rank)
        self.ui.spinBoxParentId.setValue(taxonomicItem.parentId)
        self.ui.lineEditName.setText(taxonomicItem.name)
        self.ui.lineEditCommon.setText(taxonomicItem.commonName)
        self.ui.lineEditOther.setText(taxonomicItem.otherNames)
        self.ui.plainTextEditInfo.setPlainText(taxonomicItem.information)
        if taxonomicItem.id == 0:
            self.ui.pushButtonDelete.setEnabled(False)
            self.ui.pushButtonUpdate.setEnabled(False)
            self.ui.pushButtonAquaml.setEnabled(False)
            self.ui.pushButtonTaiEOL.setEnabled(False)
        else:
            self.ui.pushButtonDelete.setEnabled(True)
            self.ui.pushButtonUpdate.setEnabled(True)
            self.ui.pushButtonAquaml.setEnabled(True)
            self.ui.pushButtonTaiEOL.setEnabled(True)

    def callback_UpdateTaxonomicItem(self, id: int):
        QMessageBox.information(self, "Information", "Item Updated Succeeded")
        self.signal_DBTaxonomicChanged.emit(id)

    def callback_DeleteTaxonomicItem(self, id: int):
        QMessageBox.information(self, "Information", "Item Deleted Succeeded")
        self.signal_DBTaxonomicChanged.emit(id)

    def callback_GetCommonNameFromAquaml(self, commonName: str):
        if commonName:
            QMessageBox.information(
                self, "Information", "Get Common Name from Aquaml Succeeded"
            )
            self.ui.lineEditCommon.setText(commonName)
        else:
            QMessageBox.information(
                self, "Information", "Get Common Name from Aquaml Failed"
            )

    def callback_GetCommonNameFromTaiEOL(self, commonName: str):
        if commonName:
            QMessageBox.information(
                self, "Information", "Get Common Name from TaiEOL Succeeded"
            )
            self.ui.lineEditCommon.setText(commonName)
        else:
            QMessageBox.information(
                self, "Information", "Get Common Name from TaiEOL Failed"
            )

    def ui_pushButtonAquaml_clicked(self):
        name = self.ui.lineEditName.text()
        self.worker.add(
            func=self.worker.GetCommonNameFromAquaml,
            para=name,
            callback=self.callback_GetCommonNameFromAquaml,
            reciever=self,
        )

    def ui_pushButtonTaiEOL_clicked(self):
        name = self.ui.lineEditName.text()
        self.worker.add(
            func=self.worker.GetCommonNameFromTaiEOL,
            para=name,
            callback=self.callback_GetCommonNameFromTaiEOL,
            reciever=self,
        )

    def ui_pushButtonDelete_clicked(self):
        result = QMessageBox.question(
            self,
            "Warning",
            "Please Confirm Delete Operation",
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Cancel,
        )
        if result != QMessageBox.StandardButton.Ok:
            return
        id = self.ui.spinBoxId.value()
        self.worker.add(
            func=self.worker.DeleteTaxonomicItem,
            para=id,
            callback=self.callback_DeleteTaxonomicItem,
            reciever=self,
        )

    def ui_pushButtonUpdate_clicked(self):
        result = QMessageBox.question(
            self,
            "Warning",
            "Please Confirm Update Operation",
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Cancel,
        )
        if result != QMessageBox.StandardButton.Ok:
            return
        taxonomicItem = TaxonomicItem(
            self.ui.spinBoxId.value(),
            self.ui.spinBoxParentId.value(),
            self.ui.lineEditName.text(),
            self.ui.lineEditRank.text(),
            self.ui.lineEditCommon.text(),
            self.ui.lineEditOther.text(),
            self.ui.plainTextEditInfo.toPlainText(),
        )
        self.worker.add(
            func=self.worker.UpdateTaxonomicItem,
            para=taxonomicItem,
            callback=self.callback_UpdateTaxonomicItem,
            reciever=self,
        )

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        return super().closeEvent(event)
