# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetDiveLog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QDateTimeEdit, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.setWindowModality(Qt.NonModal)
        widgetRoot.resize(911, 166)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        widgetRoot.setMinimumSize(QSize(0, 0))
        widgetRoot.setMaximumSize(QSize(16777215, 16777215))
        widgetRoot.setBaseSize(QSize(906, 166))
        self.horizontalLayout = QHBoxLayout(widgetRoot)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(6)
        self.label_2 = QLabel(widgetRoot)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.dateTimeEditTimeIn = QDateTimeEdit(widgetRoot)
        self.dateTimeEditTimeIn.setObjectName(u"dateTimeEditTimeIn")
        sizePolicy1.setHeightForWidth(self.dateTimeEditTimeIn.sizePolicy().hasHeightForWidth())
        self.dateTimeEditTimeIn.setSizePolicy(sizePolicy1)
        self.dateTimeEditTimeIn.setMinimumSize(QSize(200, 21))
        self.dateTimeEditTimeIn.setMaximumSize(QSize(16777215, 16777215))
        self.dateTimeEditTimeIn.setAlignment(Qt.AlignCenter)
        self.dateTimeEditTimeIn.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEditTimeIn.setDateTime(QDateTime(QDate(1990, 10, 1), QTime(0, 0, 0)))
        self.dateTimeEditTimeIn.setCalendarPopup(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateTimeEditTimeIn)

        self.label_3 = QLabel(widgetRoot)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.dateTimeEditTimeOut = QDateTimeEdit(widgetRoot)
        self.dateTimeEditTimeOut.setObjectName(u"dateTimeEditTimeOut")
        sizePolicy1.setHeightForWidth(self.dateTimeEditTimeOut.sizePolicy().hasHeightForWidth())
        self.dateTimeEditTimeOut.setSizePolicy(sizePolicy1)
        self.dateTimeEditTimeOut.setMinimumSize(QSize(200, 21))
        self.dateTimeEditTimeOut.setMaximumSize(QSize(16777215, 16777215))
        self.dateTimeEditTimeOut.setAlignment(Qt.AlignCenter)
        self.dateTimeEditTimeOut.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEditTimeOut.setDateTime(QDateTime(QDate(1990, 10, 1), QTime(0, 0, 0)))
        self.dateTimeEditTimeOut.setCurrentSection(QDateTimeEdit.YearSection)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateTimeEditTimeOut)

        self.label_4 = QLabel(widgetRoot)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboBoxLocation = QComboBox(widgetRoot)
        self.comboBoxLocation.setObjectName(u"comboBoxLocation")
        sizePolicy1.setHeightForWidth(self.comboBoxLocation.sizePolicy().hasHeightForWidth())
        self.comboBoxLocation.setSizePolicy(sizePolicy1)
        self.comboBoxLocation.setMinimumSize(QSize(200, 21))
        self.comboBoxLocation.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxLocation.setStyleSheet(u"")
        self.comboBoxLocation.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxLocation)

        self.label_5 = QLabel(widgetRoot)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.comboBoxDiveSite = QComboBox(widgetRoot)
        self.comboBoxDiveSite.setObjectName(u"comboBoxDiveSite")
        sizePolicy1.setHeightForWidth(self.comboBoxDiveSite.sizePolicy().hasHeightForWidth())
        self.comboBoxDiveSite.setSizePolicy(sizePolicy1)
        self.comboBoxDiveSite.setMinimumSize(QSize(200, 21))
        self.comboBoxDiveSite.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxDiveSite.setEditable(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxDiveSite)

        self.pushButtonInsert = QPushButton(widgetRoot)
        self.pushButtonInsert.setObjectName(u"pushButtonInsert")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonInsert.sizePolicy().hasHeightForWidth())
        self.pushButtonInsert.setSizePolicy(sizePolicy2)
        self.pushButtonInsert.setMinimumSize(QSize(200, 23))
        self.pushButtonInsert.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.pushButtonInsert)

        self.pushButtonDelete = QPushButton(widgetRoot)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy2)
        self.pushButtonDelete.setMinimumSize(QSize(200, 23))
        self.pushButtonDelete.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.pushButtonDelete)


        self.horizontalLayout.addLayout(self.formLayout)

        self.tableWidgetDiveLog = QTableWidget(widgetRoot)
        if (self.tableWidgetDiveLog.columnCount() < 4):
            self.tableWidgetDiveLog.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetDiveLog.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetDiveLog.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetDiveLog.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetDiveLog.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidgetDiveLog.rowCount() < 3):
            self.tableWidgetDiveLog.setRowCount(3)
        self.tableWidgetDiveLog.setObjectName(u"tableWidgetDiveLog")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidgetDiveLog.sizePolicy().hasHeightForWidth())
        self.tableWidgetDiveLog.setSizePolicy(sizePolicy3)
        self.tableWidgetDiveLog.setMinimumSize(QSize(0, 0))
        self.tableWidgetDiveLog.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidgetDiveLog.setFocusPolicy(Qt.NoFocus)
        self.tableWidgetDiveLog.setStyleSheet(u"::item:selected:!active { background-color: rgb(0, 120, 215);color: white;}\n"
":focus { outline: none; }")
        self.tableWidgetDiveLog.setFrameShape(QFrame.Box)
        self.tableWidgetDiveLog.setMidLineWidth(1)
        self.tableWidgetDiveLog.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidgetDiveLog.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidgetDiveLog.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetDiveLog.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidgetDiveLog.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetDiveLog.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetDiveLog.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidgetDiveLog.setGridStyle(Qt.SolidLine)
        self.tableWidgetDiveLog.setSortingEnabled(True)
        self.tableWidgetDiveLog.setWordWrap(False)
        self.tableWidgetDiveLog.setRowCount(3)
        self.tableWidgetDiveLog.setColumnCount(4)
        self.tableWidgetDiveLog.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetDiveLog.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetDiveLog.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDiveLog.verticalHeader().setVisible(True)
        self.tableWidgetDiveLog.verticalHeader().setMinimumSectionSize(20)
        self.tableWidgetDiveLog.verticalHeader().setDefaultSectionSize(20)
        self.tableWidgetDiveLog.verticalHeader().setHighlightSections(True)
        self.tableWidgetDiveLog.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidgetDiveLog.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tableWidgetDiveLog)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"DiveLog", None))
        self.label_2.setText(QCoreApplication.translate("widgetRoot", u"Time In", None))
        self.dateTimeEditTimeIn.setDisplayFormat(QCoreApplication.translate("widgetRoot", u"yyyy/MM/dd HH:mm", None))
        self.label_3.setText(QCoreApplication.translate("widgetRoot", u"Time Out", None))
        self.dateTimeEditTimeOut.setDisplayFormat(QCoreApplication.translate("widgetRoot", u"yyyy/MM/dd HH:mm", None))
        self.label_4.setText(QCoreApplication.translate("widgetRoot", u"Location", None))
        self.label_5.setText(QCoreApplication.translate("widgetRoot", u"Dive Site", None))
        self.pushButtonInsert.setText(QCoreApplication.translate("widgetRoot", u"Insert", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("widgetRoot", u"Delete", None))
        ___qtablewidgetitem = self.tableWidgetDiveLog.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widgetRoot", u"Time In", None));
        ___qtablewidgetitem1 = self.tableWidgetDiveLog.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widgetRoot", u"Time Out", None));
        ___qtablewidgetitem2 = self.tableWidgetDiveLog.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widgetRoot", u"Location", None));
        ___qtablewidgetitem3 = self.tableWidgetDiveLog.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("widgetRoot", u"Dive Site", None));
    # retranslateUi

