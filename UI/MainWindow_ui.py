# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1394, 784)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.actionExpend_All = QAction(MainWindow)
        self.actionExpend_All.setObjectName(u"actionExpend_All")
        self.actionCollapse_All = QAction(MainWindow)
        self.actionCollapse_All.setObjectName(u"actionCollapse_All")
        self.actionSet_Path = QAction(MainWindow)
        self.actionSet_Path.setObjectName(u"actionSet_Path")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 0))
        self.centralwidget.setStyleSheet(u"")
        self.layoutCentral = QVBoxLayout(self.centralwidget)
        self.layoutCentral.setSpacing(2)
        self.layoutCentral.setObjectName(u"layoutCentral")
        self.layoutCentral.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1394, 21))
        self.menuDock = QMenu(self.menubar)
        self.menuDock.setObjectName(u"menuDock")
        self.menuTaxonomic = QMenu(self.menubar)
        self.menuTaxonomic.setObjectName(u"menuTaxonomic")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetTree = QDockWidget(MainWindow)
        self.dockWidgetTree.setObjectName(u"dockWidgetTree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidgetTree.sizePolicy().hasHeightForWidth())
        self.dockWidgetTree.setSizePolicy(sizePolicy1)
        self.dockWidgetTree.setMinimumSize(QSize(81, 39))
        self.dockWidgetTree.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetTree.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetTree.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsTree = QWidget()
        self.dockWidgetContentsTree.setObjectName(u"dockWidgetContentsTree")
        self.layoutDockWidgetTree = QVBoxLayout(self.dockWidgetContentsTree)
        self.layoutDockWidgetTree.setSpacing(2)
        self.layoutDockWidgetTree.setObjectName(u"layoutDockWidgetTree")
        self.layoutDockWidgetTree.setSizeConstraint(QLayout.SetMinimumSize)
        self.layoutDockWidgetTree.setContentsMargins(0, 0, 0, 0)
        self.dockWidgetTree.setWidget(self.dockWidgetContentsTree)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidgetTree)
        self.dockWidgetInsert = QDockWidget(MainWindow)
        self.dockWidgetInsert.setObjectName(u"dockWidgetInsert")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dockWidgetInsert.sizePolicy().hasHeightForWidth())
        self.dockWidgetInsert.setSizePolicy(sizePolicy2)
        self.dockWidgetInsert.setMinimumSize(QSize(81, 39))
        self.dockWidgetInsert.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetInsert.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsInsert = QWidget()
        self.dockWidgetContentsInsert.setObjectName(u"dockWidgetContentsInsert")
        self.layoutDockWidgetInsert = QVBoxLayout(self.dockWidgetContentsInsert)
        self.layoutDockWidgetInsert.setSpacing(2)
        self.layoutDockWidgetInsert.setObjectName(u"layoutDockWidgetInsert")
        self.layoutDockWidgetInsert.setSizeConstraint(QLayout.SetMinimumSize)
        self.layoutDockWidgetInsert.setContentsMargins(0, 0, 0, 0)
        self.dockWidgetInsert.setWidget(self.dockWidgetContentsInsert)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidgetInsert)
        self.dockWidgetSearch = QDockWidget(MainWindow)
        self.dockWidgetSearch.setObjectName(u"dockWidgetSearch")
        sizePolicy2.setHeightForWidth(self.dockWidgetSearch.sizePolicy().hasHeightForWidth())
        self.dockWidgetSearch.setSizePolicy(sizePolicy2)
        self.dockWidgetSearch.setMinimumSize(QSize(81, 39))
        self.dockWidgetSearch.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetSearch.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsSearch = QWidget()
        self.dockWidgetContentsSearch.setObjectName(u"dockWidgetContentsSearch")
        self.layoutDockWidgetSearch = QVBoxLayout(self.dockWidgetContentsSearch)
        self.layoutDockWidgetSearch.setSpacing(2)
        self.layoutDockWidgetSearch.setObjectName(u"layoutDockWidgetSearch")
        self.layoutDockWidgetSearch.setSizeConstraint(QLayout.SetMinimumSize)
        self.layoutDockWidgetSearch.setContentsMargins(0, 0, 0, 0)
        self.dockWidgetSearch.setWidget(self.dockWidgetContentsSearch)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidgetSearch)
        self.dockWidgetUpdate = QDockWidget(MainWindow)
        self.dockWidgetUpdate.setObjectName(u"dockWidgetUpdate")
        sizePolicy2.setHeightForWidth(self.dockWidgetUpdate.sizePolicy().hasHeightForWidth())
        self.dockWidgetUpdate.setSizePolicy(sizePolicy2)
        self.dockWidgetUpdate.setMinimumSize(QSize(81, 39))
        self.dockWidgetUpdate.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetUpdate.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsUpdate = QWidget()
        self.dockWidgetContentsUpdate.setObjectName(u"dockWidgetContentsUpdate")
        self.dockWidgetContentsUpdate.setStyleSheet(u"")
        self.layoutDockWidgetUpdate = QVBoxLayout(self.dockWidgetContentsUpdate)
        self.layoutDockWidgetUpdate.setSpacing(2)
        self.layoutDockWidgetUpdate.setObjectName(u"layoutDockWidgetUpdate")
        self.layoutDockWidgetUpdate.setSizeConstraint(QLayout.SetMinimumSize)
        self.layoutDockWidgetUpdate.setContentsMargins(0, 0, 0, 0)
        self.dockWidgetUpdate.setWidget(self.dockWidgetContentsUpdate)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidgetUpdate)
        self.dockWidgetDiveLog = QDockWidget(MainWindow)
        self.dockWidgetDiveLog.setObjectName(u"dockWidgetDiveLog")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dockWidgetDiveLog.sizePolicy().hasHeightForWidth())
        self.dockWidgetDiveLog.setSizePolicy(sizePolicy3)
        self.dockWidgetDiveLog.setMinimumSize(QSize(81, 193))
        self.dockWidgetDiveLog.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetDiveLog.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsDiveLog = QWidget()
        self.dockWidgetContentsDiveLog.setObjectName(u"dockWidgetContentsDiveLog")
        sizePolicy3.setHeightForWidth(self.dockWidgetContentsDiveLog.sizePolicy().hasHeightForWidth())
        self.dockWidgetContentsDiveLog.setSizePolicy(sizePolicy3)
        self.dockWidgetContentsDiveLog.setMinimumSize(QSize(0, 170))
        self.dockWidgetContentsDiveLog.setMaximumSize(QSize(16777215, 16777215))
        self.layoutDockWidgetDivelog = QHBoxLayout(self.dockWidgetContentsDiveLog)
        self.layoutDockWidgetDivelog.setSpacing(2)
        self.layoutDockWidgetDivelog.setObjectName(u"layoutDockWidgetDivelog")
        self.layoutDockWidgetDivelog.setContentsMargins(0, 0, 0, 2)
        self.dockWidgetDiveLog.setWidget(self.dockWidgetContentsDiveLog)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidgetDiveLog)
        self.dockWidgetGallery = QDockWidget(MainWindow)
        self.dockWidgetGallery.setObjectName(u"dockWidgetGallery")
        self.dockWidgetGallery.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsGallery = QWidget()
        self.dockWidgetContentsGallery.setObjectName(u"dockWidgetContentsGallery")
        self.layoutDockWidgetGallery = QVBoxLayout(self.dockWidgetContentsGallery)
        self.layoutDockWidgetGallery.setSpacing(2)
        self.layoutDockWidgetGallery.setObjectName(u"layoutDockWidgetGallery")
        self.layoutDockWidgetGallery.setContentsMargins(0, 0, 0, 0)
        self.dockWidgetGallery.setWidget(self.dockWidgetContentsGallery)
        MainWindow.addDockWidget(Qt.TopDockWidgetArea, self.dockWidgetGallery)
        self.dockWidgetAlbum = QDockWidget(MainWindow)
        self.dockWidgetAlbum.setObjectName(u"dockWidgetAlbum")
        self.dockWidgetAlbum.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContentsAlbum = QWidget()
        self.dockWidgetContentsAlbum.setObjectName(u"dockWidgetContentsAlbum")
        self.layoutDockWidgetAlbum = QVBoxLayout(self.dockWidgetContentsAlbum)
        self.layoutDockWidgetAlbum.setSpacing(2)
        self.layoutDockWidgetAlbum.setObjectName(u"layoutDockWidgetAlbum")
        self.layoutDockWidgetAlbum.setContentsMargins(0, 0, 0, 0)
        self.dockWidgetAlbum.setWidget(self.dockWidgetContentsAlbum)
        MainWindow.addDockWidget(Qt.TopDockWidgetArea, self.dockWidgetAlbum)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDock.menuAction())
        self.menubar.addAction(self.menuTaxonomic.menuAction())
        self.menuTaxonomic.addAction(self.actionExpend_All)
        self.menuTaxonomic.addAction(self.actionCollapse_All)
        self.menuFile.addAction(self.actionSet_Path)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExpend_All.setText(QCoreApplication.translate("MainWindow", u"Expend All", None))
        self.actionCollapse_All.setText(QCoreApplication.translate("MainWindow", u"Collapse All", None))
        self.actionSet_Path.setText(QCoreApplication.translate("MainWindow", u"Set Path", None))
        self.menuDock.setTitle(QCoreApplication.translate("MainWindow", u"Dock", None))
        self.menuTaxonomic.setTitle(QCoreApplication.translate("MainWindow", u"Taxonomic", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.dockWidgetTree.setWindowTitle(QCoreApplication.translate("MainWindow", u"Taxonomic Tree", None))
        self.dockWidgetInsert.setWindowTitle(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.dockWidgetSearch.setWindowTitle(QCoreApplication.translate("MainWindow", u"Search", None))
        self.dockWidgetUpdate.setWindowTitle(QCoreApplication.translate("MainWindow", u"Update", None))
        self.dockWidgetDiveLog.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dive Log", None))
        self.dockWidgetGallery.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gallery", None))
        self.dockWidgetAlbum.setWindowTitle(QCoreApplication.translate("MainWindow", u"Album", None))
    # retranslateUi

