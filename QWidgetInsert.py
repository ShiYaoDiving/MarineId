from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from PySide6.QtGui import QCloseEvent

from UI.QWidgetInsert_ui import Ui_widgetRoot
from GlobalType import CallbackEvent, TaxonomicPath
from WorkerInsert import WorkerInsert


class QWidgetInsert(QWidget):
    signal_DBTaxonomicChanged = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        # Class Member
        self.ui = Ui_widgetRoot()
        self.workPath = Path().resolve().parent.joinpath("data")
        self.worker = WorkerInsert(self.workPath)
        self.worker.start()
        # UI Init
        self.ui.setupUi(self)
        # UI Singal -> Slot
        self.ui.pushButtonDB.clicked.connect(self.ui_pushButtonDB_clicked)
        self.ui.pushButtonWoRMS.clicked.connect(self.ui_pushButtonWoRMS_clicked)
        self.ui.pushButtonGBIF.clicked.connect(self.ui_pushButtonGBIF_clicked)
        self.ui.pushButtonInsert.clicked.connect(self.ui_pushButtonInsert_clicked)

    def callback_GetTaxonomicPath(self, taxonomicPath: TaxonomicPath):
        if taxonomicPath.Species:
            self.ui.lineEditKingdom.setText(taxonomicPath.Kingdom)
            self.ui.lineEditPhylum.setText(taxonomicPath.Phylum)
            self.ui.lineEditClass.setText(taxonomicPath.Class)
            self.ui.lineEditOrder.setText(taxonomicPath.Order)
            self.ui.lineEditFamily.setText(taxonomicPath.Family)
            self.ui.lineEditGenus.setText(taxonomicPath.Genus)
            self.ui.lineEditSpecies.setText(taxonomicPath.Species)
            if taxonomicPath.Status != "accepted":
                QMessageBox.information(
                    self, "Information", "Species Found but Unaccepted"
                )
            else:
                QMessageBox.information(self, "Information", "Species Found")
        else:
            QMessageBox.warning(self, "Warning", "Species Not Found")
        pass

    def callback_InsertTaxonomicPath(self, id: int):
        QMessageBox.information(self, "Information", "Insert Succeeded")
        self.signal_DBTaxonomicChanged.emit(id)

    def ui_pushButtonDB_clicked(self):
        self.worker.add(
            func=self.worker.GetTaxonomicPathFromDB,
            para=self.ui.lineEditSpecies.text().strip(),
            callback=self.callback_GetTaxonomicPath,
            reciever=self,
        )

    def ui_pushButtonWoRMS_clicked(self):
        self.worker.add(
            func=self.worker.GetTaxonomicPathFromWoRMS,
            para=self.ui.lineEditSpecies.text().strip(),
            callback=self.callback_GetTaxonomicPath,
            reciever=self,
        )

    def ui_pushButtonGBIF_clicked(self):
        self.worker.add(
            func=self.worker.GetTaxonomicPathFromGBIF,
            para=self.ui.lineEditSpecies.text().strip(),
            callback=self.callback_GetTaxonomicPath,
            reciever=self,
        )

    def ui_pushButtonInsert_clicked(self):
        taxonomicPath = TaxonomicPath(
            self.ui.lineEditKingdom.text().strip(),
            self.ui.lineEditPhylum.text().strip(),
            self.ui.lineEditClass.text().strip(),
            self.ui.lineEditOrder.text().strip(),
            self.ui.lineEditFamily.text().strip(),
            self.ui.lineEditGenus.text().strip(),
            self.ui.lineEditSpecies.text().strip(),
        )
        if taxonomicPath.NoBlankField():
            self.worker.add(
                func=self.worker.InsertTaxonomicPath,
                para=taxonomicPath,
                callback=self.callback_InsertTaxonomicPath,
                reciever=self,
            )
        else:
            QMessageBox.warning(self, "Warning", "Field cannot be Empty")
        pass

    def customEvent(self, event: CallbackEvent) -> None:
        QApplication.restoreOverrideCursor()
        event.callback(event.para)
        return super().customEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.worker.stop()
        self.worker.wait()
        return super().closeEvent(event)
