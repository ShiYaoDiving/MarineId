from pathlib import Path

from PySide6.QtCore import Qt, QDateTime, Signal, Slot
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QApplication
from PySide6.QtGui import QCloseEvent

from UI.QWidgetDiveLog_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, DiveLog
from WorkerDiveLog import WorkerDiveLog


class QWidgetDiveLog(QWidget):
    signal_DBDiveLogChanged = Signal()

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerDiveLog(self.workPath)
        self.worker.start()
        self.diveLogList: list[DiveLog] = []
        self.idToSelect = 0
        # UI Init
        self.ui.setupUi(self)
        self.ui.comboBoxLocation.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.comboBoxDiveSite.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        # UI Singal -> Slot
        self.ui.comboBoxLocation.editTextChanged.connect(
            self.ui_comboBoxLocation_editTextChanged
        )
        self.ui.dateTimeEditTimeIn.editingFinished.connect(
            self.ui_dateTimeEditTimeIn_editingFinished
        )
        self.ui.dateTimeEditTimeOut.editingFinished.connect(
            self.ui_dateTimeEditTimeOut_editingFinished
        )
        self.ui.pushButtonInsert.clicked.connect(self.ui_pushButtonInsert_clicked)
        self.ui.pushButtonDelete.clicked.connect(self.ui_pushButtonDelete_clicked)
        self.ui.tableWidgetDiveLog.itemSelectionChanged.connect(
            self.ui_tableWidgetDiveLog_itemSelectionChanged
        )
        # Init Table
        self.worker.add(
            func=self.worker.GetDiveLogList,
            para=None,
            callback=self.callback_GetDiveLogList,
            reciever=self,
        )

    def callback_GetDiveLogList(self, diveLogList: list[DiveLog]):
        self.diveLogList = diveLogList
        self.ui.tableWidgetDiveLog.clearSelection()
        self.ui.tableWidgetDiveLog.clearContents()
        self.ui.tableWidgetDiveLog.setSortingEnabled(False)
        self.ui.tableWidgetDiveLog.setRowCount(len(self.diveLogList))
        for index, diveLog in enumerate(self.diveLogList):
            itemTimeIn = QTableWidgetItem(diveLog.timeIn.toString("yyyy-MM-dd hh:mm"))
            itemTimeIn.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            itemTimeIn.setData(Qt.ItemDataRole.UserRole, diveLog)
            itemTimeOut = QTableWidgetItem(diveLog.timeOut.toString("yyyy-MM-dd hh:mm"))
            itemTimeOut.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            itemDiveLocation = QTableWidgetItem(diveLog.location)
            itemDiveLocation.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            itemDiveSite = QTableWidgetItem(diveLog.diveSite)
            itemDiveSite.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.tableWidgetDiveLog.setItem(index, 0, itemTimeIn)
            self.ui.tableWidgetDiveLog.setItem(index, 1, itemTimeOut)
            self.ui.tableWidgetDiveLog.setItem(index, 2, itemDiveLocation)
            self.ui.tableWidgetDiveLog.setItem(index, 3, itemDiveSite)
        self.ui.tableWidgetDiveLog.setSortingEnabled(True)
        for row in reversed(range(self.ui.tableWidgetDiveLog.rowCount())):
            item: QTableWidgetItem = self.ui.tableWidgetDiveLog.item(row, 0)
            diveLog: DiveLog = item.data(Qt.ItemDataRole.UserRole)
            if diveLog.id == self.idToSelect:
                break
        self.ui.tableWidgetDiveLog.selectRow(row)
        lastLocation = self.ui.comboBoxLocation.currentText()
        locationList = DiveLog.GetLocationList(self.diveLogList)
        self.ui.comboBoxLocation.clear()
        for index, location in enumerate(locationList):
            self.ui.comboBoxLocation.addItem(location)
            self.ui.comboBoxLocation.setItemData(
                index, Qt.AlignmentFlag.AlignCenter, Qt.ItemDataRole.TextAlignmentRole
            )
        self.ui.comboBoxLocation.setCurrentText(lastLocation)

    def callback_InsertDiveLog(self, id: int):
        QMessageBox.information(self, "Information", "Insert Succeeded")
        self.idToSelect = id
        self.worker.add(
            func=self.worker.GetDiveLogList,
            para=None,
            callback=self.callback_GetDiveLogList,
            reciever=self,
        )
        self.signal_DBDiveLogChanged.emit()

    def callback_DeleteDiveLog(self, para):
        QMessageBox.information(self, "Information", "Delete Succeeded")
        self.idToSelect = 1
        self.worker.add(
            func=self.worker.GetDiveLogList,
            para=None,
            callback=self.callback_GetDiveLogList,
            reciever=self,
        )

    def ui_comboBoxLocation_editTextChanged(self, text):
        diveSiteList = DiveLog.GetDiveSiteListByLocation(self.diveLogList, text)
        self.ui.comboBoxDiveSite.clear()
        for index, diveSite in enumerate(diveSiteList):
            self.ui.comboBoxDiveSite.addItem(diveSite)
            self.ui.comboBoxDiveSite.setItemData(
                index, Qt.AlignmentFlag.AlignCenter, Qt.ItemDataRole.TextAlignmentRole
            )
        self.ui.comboBoxDiveSite.setCurrentIndex(0)

    def ui_dateTimeEditTimeIn_editingFinished(self):
        if (
            self.ui.dateTimeEditTimeOut.dateTime()
            < self.ui.dateTimeEditTimeIn.dateTime()
        ):
            self.ui.dateTimeEditTimeOut.setDateTime(
                self.ui.dateTimeEditTimeIn.dateTime()
            )
        pass

    def ui_dateTimeEditTimeOut_editingFinished(self):
        if (
            self.ui.dateTimeEditTimeIn.dateTime()
            > self.ui.dateTimeEditTimeOut.dateTime()
        ):
            self.ui.dateTimeEditTimeIn.setDateTime(
                self.ui.dateTimeEditTimeOut.dateTime()
            )
        pass

    def ui_pushButtonInsert_clicked(self):
        diveLog = DiveLog(
            -1,
            self.ui.dateTimeEditTimeIn.dateTime(),
            self.ui.dateTimeEditTimeOut.dateTime(),
            self.ui.comboBoxLocation.currentText(),
            self.ui.comboBoxDiveSite.currentText(),
        )
        self.worker.add(
            func=self.worker.InsertDiveLog,
            para=diveLog,
            callback=self.callback_InsertDiveLog,
            reciever=self,
        )
        pass

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
        selectedItems = self.ui.tableWidgetDiveLog.selectedItems()
        if selectedItems:
            diveLog: DiveLog = selectedItems[0].data(Qt.ItemDataRole.UserRole)
        self.worker.add(
            func=self.worker.DeleteDiveLog,
            para=diveLog.id,
            callback=self.callback_DeleteDiveLog,
            reciever=self,
        )
        pass

    def ui_tableWidgetDiveLog_itemSelectionChanged(self):
        selectedItems = self.ui.tableWidgetDiveLog.selectedItems()
        if selectedItems:
            diveLog: DiveLog = selectedItems[0].data(Qt.ItemDataRole.UserRole)
            self.ui.dateTimeEditTimeIn.setDateTime(diveLog.timeIn)
            self.ui.dateTimeEditTimeOut.setDateTime(QDateTime(diveLog.timeOut))
            self.ui.comboBoxLocation.setEditText(diveLog.location)
            self.ui.comboBoxDiveSite.setEditText(diveLog.diveSite)

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        return super().closeEvent(event)
