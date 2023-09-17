# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetSearch.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QGridLayout,
    QLayout, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.resize(230, 264)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(widgetRoot)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(2, 1, 2, 1)
        self.lineEditKeyword = QLineEdit(widgetRoot)
        self.lineEditKeyword.setObjectName(u"lineEditKeyword")
        self.lineEditKeyword.setMinimumSize(QSize(0, 21))
        self.lineEditKeyword.setStyleSheet(u"")
        self.lineEditKeyword.setAlignment(Qt.AlignCenter)
        self.lineEditKeyword.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditKeyword, 0, 0, 1, 1)

        self.pushButtonSearch = QPushButton(widgetRoot)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")
        self.pushButtonSearch.setEnabled(False)
        self.pushButtonSearch.setMinimumSize(QSize(53, 23))
        self.pushButtonSearch.setMaximumSize(QSize(53, 16777215))

        self.gridLayout.addWidget(self.pushButtonSearch, 0, 1, 1, 1)

        self.listWidgetResult = QListWidget(widgetRoot)
        self.listWidgetResult.setObjectName(u"listWidgetResult")
        sizePolicy.setHeightForWidth(self.listWidgetResult.sizePolicy().hasHeightForWidth())
        self.listWidgetResult.setSizePolicy(sizePolicy)
        self.listWidgetResult.setMinimumSize(QSize(0, 0))
        self.listWidgetResult.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidgetResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidgetResult.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetResult.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidgetResult.setIconSize(QSize(0, 1))
        self.listWidgetResult.setLayoutMode(QListView.SinglePass)
        self.listWidgetResult.setViewMode(QListView.ListMode)
        self.listWidgetResult.setItemAlignment(Qt.AlignLeading)
        self.listWidgetResult.setSortingEnabled(True)

        self.gridLayout.addWidget(self.listWidgetResult, 1, 0, 1, 2)


        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.pushButtonSearch.setText(QCoreApplication.translate("widgetRoot", u"Search", None))
    # retranslateUi

