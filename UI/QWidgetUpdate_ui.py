# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetUpdate.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.resize(312, 262)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        widgetRoot.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(widgetRoot)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(widgetRoot)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEditOther = QLineEdit(widgetRoot)
        self.lineEditOther.setObjectName(u"lineEditOther")
        self.lineEditOther.setMinimumSize(QSize(0, 21))
        self.lineEditOther.setStyleSheet(u"")
        self.lineEditOther.setAlignment(Qt.AlignCenter)
        self.lineEditOther.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditOther, 5, 1, 1, 1)

        self.spinBoxId = QSpinBox(widgetRoot)
        self.spinBoxId.setObjectName(u"spinBoxId")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBoxId.sizePolicy().hasHeightForWidth())
        self.spinBoxId.setSizePolicy(sizePolicy2)
        self.spinBoxId.setMinimumSize(QSize(0, 21))
        self.spinBoxId.setAutoFillBackground(False)
        self.spinBoxId.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.spinBoxId.setAlignment(Qt.AlignCenter)
        self.spinBoxId.setReadOnly(True)
        self.spinBoxId.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxId.setMaximum(9999)

        self.gridLayout.addWidget(self.spinBoxId, 0, 1, 1, 1)

        self.label = QLabel(widgetRoot)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.plainTextEditInfo = QPlainTextEdit(widgetRoot)
        self.plainTextEditInfo.setObjectName(u"plainTextEditInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plainTextEditInfo.sizePolicy().hasHeightForWidth())
        self.plainTextEditInfo.setSizePolicy(sizePolicy3)
        self.plainTextEditInfo.setMinimumSize(QSize(0, 0))
        self.plainTextEditInfo.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEditInfo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEditInfo.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEditInfo.setOverwriteMode(False)
        self.plainTextEditInfo.setTabStopDistance(80.000000000000000)
        self.plainTextEditInfo.setCursorWidth(1)
        self.plainTextEditInfo.setMaximumBlockCount(0)

        self.gridLayout.addWidget(self.plainTextEditInfo, 6, 1, 1, 1)

        self.spinBoxParentId = QSpinBox(widgetRoot)
        self.spinBoxParentId.setObjectName(u"spinBoxParentId")
        sizePolicy2.setHeightForWidth(self.spinBoxParentId.sizePolicy().hasHeightForWidth())
        self.spinBoxParentId.setSizePolicy(sizePolicy2)
        self.spinBoxParentId.setMinimumSize(QSize(0, 21))
        self.spinBoxParentId.setAutoFillBackground(False)
        self.spinBoxParentId.setStyleSheet(u"")
        self.spinBoxParentId.setAlignment(Qt.AlignCenter)
        self.spinBoxParentId.setReadOnly(False)
        self.spinBoxParentId.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxParentId.setMaximum(9999)

        self.gridLayout.addWidget(self.spinBoxParentId, 2, 1, 1, 1)

        self.lineEditCommon = QLineEdit(widgetRoot)
        self.lineEditCommon.setObjectName(u"lineEditCommon")
        self.lineEditCommon.setMinimumSize(QSize(0, 21))
        self.lineEditCommon.setStyleSheet(u"")
        self.lineEditCommon.setAlignment(Qt.AlignCenter)
        self.lineEditCommon.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditCommon, 4, 1, 1, 1)

        self.lineEditRank = QLineEdit(widgetRoot)
        self.lineEditRank.setObjectName(u"lineEditRank")
        self.lineEditRank.setMinimumSize(QSize(0, 21))
        self.lineEditRank.setStyleSheet(u"")
        self.lineEditRank.setAlignment(Qt.AlignCenter)
        self.lineEditRank.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditRank, 3, 1, 1, 1)

        self.label_5 = QLabel(widgetRoot)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(widgetRoot)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_7 = QLabel(widgetRoot)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.lineEditName = QLineEdit(widgetRoot)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setMinimumSize(QSize(0, 21))
        self.lineEditName.setStyleSheet(u"")
        self.lineEditName.setAlignment(Qt.AlignCenter)
        self.lineEditName.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 1)

        self.label_6 = QLabel(widgetRoot)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_4 = QLabel(widgetRoot)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAquaml = QPushButton(widgetRoot)
        self.pushButtonAquaml.setObjectName(u"pushButtonAquaml")
        self.pushButtonAquaml.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButtonAquaml)

        self.pushButtonTaiEOL = QPushButton(widgetRoot)
        self.pushButtonTaiEOL.setObjectName(u"pushButtonTaiEOL")
        self.pushButtonTaiEOL.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButtonTaiEOL)

        self.pushButtonDelete = QPushButton(widgetRoot)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(23)
        sizePolicy4.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy4)
        self.pushButtonDelete.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.pushButtonUpdate = QPushButton(widgetRoot)
        self.pushButtonUpdate.setObjectName(u"pushButtonUpdate")
        self.pushButtonUpdate.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.pushButtonUpdate.sizePolicy().hasHeightForWidth())
        self.pushButtonUpdate.setSizePolicy(sizePolicy4)
        self.pushButtonUpdate.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.pushButtonUpdate)

        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        QWidget.setTabOrder(self.spinBoxId, self.lineEditName)
        QWidget.setTabOrder(self.lineEditName, self.spinBoxParentId)
        QWidget.setTabOrder(self.spinBoxParentId, self.lineEditRank)
        QWidget.setTabOrder(self.lineEditRank, self.lineEditCommon)
        QWidget.setTabOrder(self.lineEditCommon, self.lineEditOther)
        QWidget.setTabOrder(self.lineEditOther, self.plainTextEditInfo)
        QWidget.setTabOrder(self.plainTextEditInfo, self.pushButtonAquaml)
        QWidget.setTabOrder(self.pushButtonAquaml, self.pushButtonDelete)
        QWidget.setTabOrder(self.pushButtonDelete, self.pushButtonUpdate)

        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("widgetRoot", u"Rank", None))
        self.label.setText(QCoreApplication.translate("widgetRoot", u"Id", None))
        self.plainTextEditInfo.setDocumentTitle("")
        self.plainTextEditInfo.setPlainText("")
        self.label_5.setText(QCoreApplication.translate("widgetRoot", u"Common", None))
        self.label_2.setText(QCoreApplication.translate("widgetRoot", u"ParentId", None))
        self.label_7.setText(QCoreApplication.translate("widgetRoot", u"Info", None))
        self.label_6.setText(QCoreApplication.translate("widgetRoot", u"Other", None))
        self.label_4.setText(QCoreApplication.translate("widgetRoot", u"Name", None))
        self.pushButtonAquaml.setText(QCoreApplication.translate("widgetRoot", u"Aquaml", None))
        self.pushButtonTaiEOL.setText(QCoreApplication.translate("widgetRoot", u"TaiEOL", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("widgetRoot", u"Delete", None))
        self.pushButtonUpdate.setText(QCoreApplication.translate("widgetRoot", u"Update", None))
    # retranslateUi

