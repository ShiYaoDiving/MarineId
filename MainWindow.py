import sys
from queue import Queue
from pathlib import Path
from PySide6.QtCore import Qt, QThread, QObject, Signal, Slot
from PySide6.QtGui import QCloseEvent, QResizeEvent
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolButton,
    QMenu,
    QSpacerItem,
    QTabWidget,
)

from QWidgetDiveLog import QWidgetDiveLog
from QWidgetTree import QWidgetTree
from QWidgetInsert import QWidgetInsert
from QWidgetUpdate import QWidgetUpdate
from QWidgetSearch import QWidgetSearch
from QWidgetGallery import QWidgetGallery
from QWidgetAlbum import QWidgetAlbum

from UI.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Class Member
        self.ui = Ui_MainWindow()
        self.qWidgetDiveLog = QWidgetDiveLog()
        self.qWidgetTree = QWidgetTree()
        self.qWidgetInsert = QWidgetInsert()
        self.qWidgetUpdate = QWidgetUpdate()
        self.qWidgetSearch = QWidgetSearch()
        self.qWidgetGallery = QWidgetGallery()
        self.qWidgetAlbum = QWidgetAlbum()
        # UI Init
        self.ui.setupUi(self)

        self.ui.layoutDockWidgetDivelog.addWidget(self.qWidgetDiveLog)
        self.ui.layoutDockWidgetTree.addWidget(self.qWidgetTree)
        self.ui.layoutDockWidgetInsert.addWidget(self.qWidgetInsert)
        self.ui.layoutDockWidgetUpdate.addWidget(self.qWidgetUpdate)
        self.ui.layoutDockWidgetSearch.addWidget(self.qWidgetSearch)
        self.ui.layoutDockWidgetGallery.addWidget(self.qWidgetGallery)
        self.ui.layoutDockWidgetAlbum.addWidget(self.qWidgetAlbum)

        self.setCorner(Qt.Corner.BottomLeftCorner, Qt.DockWidgetArea.LeftDockWidgetArea)
        self.setCorner(Qt.Corner.TopLeftCorner, Qt.DockWidgetArea.LeftDockWidgetArea)

        self.splitDockWidget(
            self.ui.dockWidgetTree,
            self.ui.dockWidgetSearch,
            Qt.Orientation.Vertical,
        )
        self.tabifyDockWidget(self.ui.dockWidgetSearch, self.ui.dockWidgetInsert)
        self.tabifyDockWidget(self.ui.dockWidgetInsert, self.ui.dockWidgetUpdate)
        self.ui.dockWidgetSearch.raise_()
        self.resizeDocks(
            [
                self.ui.dockWidgetTree,
                self.ui.dockWidgetSearch,
                self.ui.dockWidgetInsert,
                self.ui.dockWidgetUpdate,
            ],
            [
                self.ui.dockWidgetTree.maximumHeight(),
                self.ui.dockWidgetSearch.minimumHeight(),
                self.ui.dockWidgetInsert.minimumHeight(),
                self.ui.dockWidgetUpdate.minimumHeight(),
            ],
            Qt.Orientation.Vertical,
        )

        self.splitDockWidget(
            self.ui.dockWidgetGallery,
            self.ui.dockWidgetDiveLog,
            Qt.Orientation.Vertical,
        )

        self.tabifyDockWidget(self.ui.dockWidgetGallery, self.ui.dockWidgetAlbum)
        self.setTabPosition(
            Qt.DockWidgetArea.TopDockWidgetArea, QTabWidget.TabPosition.East
        )
        self.ui.dockWidgetGallery.raise_()

        self.resizeDocks(
            [
                self.ui.dockWidgetDiveLog,
                self.ui.dockWidgetGallery,
            ],
            [
                self.ui.dockWidgetDiveLog.minimumHeight(),
                self.ui.dockWidgetGallery.maximumHeight(),
            ],
            Qt.Orientation.Vertical,
        )

        self.ui.dockWidgetDiveLog.close()

        self.ui.menuDock.addAction(self.ui.dockWidgetTree.toggleViewAction())
        self.ui.menuDock.addAction(self.ui.dockWidgetInsert.toggleViewAction())
        self.ui.menuDock.addAction(self.ui.dockWidgetSearch.toggleViewAction())
        self.ui.menuDock.addAction(self.ui.dockWidgetUpdate.toggleViewAction())
        self.ui.menuDock.addAction(self.ui.dockWidgetDiveLog.toggleViewAction())
        self.ui.menuDock.addAction(self.ui.dockWidgetAlbum.toggleViewAction())
        self.ui.menuDock.addAction(self.ui.dockWidgetGallery.toggleViewAction())

        # Signal & Slot
        self.ui.actionExpend_All.triggered.connect(
            self.qWidgetTree.ui.treeWidgetTaxonomic.expandAll
        )
        self.ui.actionCollapse_All.triggered.connect(
            self.qWidgetTree.ui.treeWidgetTaxonomic.collapseAll
        )

        self.qWidgetInsert.signal_DBTaxonomicChanged.connect(
            self.qWidgetTree.slot_DbTaxonomicChanged
        )
        self.qWidgetTree.signal_ItemSelectionChanged.connect(
            self.qWidgetUpdate.slot_ItemSelectionChanged
        )
        self.qWidgetUpdate.signal_DBTaxonomicChanged.connect(
            self.qWidgetTree.slot_DbTaxonomicChanged
        )
        self.qWidgetSearch.signal_SearchResultSelected.connect(
            self.qWidgetTree.slot_SearchResultSelected
        )
        self.qWidgetTree.signal_ItemSelectionChanged.connect(
            self.qWidgetGallery.slot_ItemSelectionChanged
        )

        self.qWidgetTree.signal_ItemSelectionChanged.connect(
            self.slot_qWidgetTree_ItemSelectionChanged
        )
        self.qWidgetGallery.signal_ItemSelectionChanged.connect(
            self.slot_qWidgetGallery_ItemSelectionChanged
        )

        self.qWidgetGallery.signal_ItemSelectionChanged.connect(
            self.qWidgetAlbum.slot_ItemSelectionChanged
        )

        self.qWidgetAlbum.signal_AlbumCoverChanged.connect(
            self.qWidgetGallery.slot_AlbumCoverChanged
        )

        self.qWidgetGallery.signal_ItemSelectionChanged.connect(
            self.qWidgetTree.slot_GalleryItemSelected
        )

        # Sub Thread

    @Slot()
    def slot_qWidgetGallery_ItemSelectionChanged(self):
        self.ui.dockWidgetAlbum.raise_()

    @Slot()
    def slot_qWidgetTree_ItemSelectionChanged(self):
        self.ui.dockWidgetGallery.raise_()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.qWidgetDiveLog.closeEvent(event)
        self.qWidgetTree.closeEvent(event)
        self.qWidgetInsert.closeEvent(event)
        self.qWidgetUpdate.closeEvent(event)
        self.qWidgetSearch.closeEvent(event)
        self.qWidgetGallery.closeEvent(event)
        self.qWidgetAlbum.closeEvent(event)
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
