# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetInsert.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.resize(235, 229)
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
        self.label = QLabel(widgetRoot)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEditSpecies = QLineEdit(widgetRoot)
        self.lineEditSpecies.setObjectName(u"lineEditSpecies")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditSpecies.sizePolicy().hasHeightForWidth())
        self.lineEditSpecies.setSizePolicy(sizePolicy2)
        self.lineEditSpecies.setMinimumSize(QSize(0, 21))
        self.lineEditSpecies.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEditSpecies, 0, 1, 1, 1)

        self.label_2 = QLabel(widgetRoot)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEditKingdom = QLineEdit(widgetRoot)
        self.lineEditKingdom.setObjectName(u"lineEditKingdom")
        self.lineEditKingdom.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lineEditKingdom.sizePolicy().hasHeightForWidth())
        self.lineEditKingdom.setSizePolicy(sizePolicy2)
        self.lineEditKingdom.setMinimumSize(QSize(0, 21))
        self.lineEditKingdom.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditKingdom.setBaseSize(QSize(0, 0))
        self.lineEditKingdom.setAutoFillBackground(False)
        self.lineEditKingdom.setStyleSheet(u"")
        self.lineEditKingdom.setAlignment(Qt.AlignCenter)
        self.lineEditKingdom.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditKingdom, 1, 1, 1, 1)

        self.label_3 = QLabel(widgetRoot)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEditPhylum = QLineEdit(widgetRoot)
        self.lineEditPhylum.setObjectName(u"lineEditPhylum")
        sizePolicy2.setHeightForWidth(self.lineEditPhylum.sizePolicy().hasHeightForWidth())
        self.lineEditPhylum.setSizePolicy(sizePolicy2)
        self.lineEditPhylum.setMinimumSize(QSize(0, 21))
        self.lineEditPhylum.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditPhylum.setStyleSheet(u"")
        self.lineEditPhylum.setAlignment(Qt.AlignCenter)
        self.lineEditPhylum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditPhylum, 2, 1, 1, 1)

        self.label_5 = QLabel(widgetRoot)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEditClass = QLineEdit(widgetRoot)
        self.lineEditClass.setObjectName(u"lineEditClass")
        sizePolicy2.setHeightForWidth(self.lineEditClass.sizePolicy().hasHeightForWidth())
        self.lineEditClass.setSizePolicy(sizePolicy2)
        self.lineEditClass.setMinimumSize(QSize(0, 21))
        self.lineEditClass.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditClass.setStyleSheet(u"")
        self.lineEditClass.setAlignment(Qt.AlignCenter)
        self.lineEditClass.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditClass, 3, 1, 1, 1)

        self.label_4 = QLabel(widgetRoot)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEditOrder = QLineEdit(widgetRoot)
        self.lineEditOrder.setObjectName(u"lineEditOrder")
        sizePolicy2.setHeightForWidth(self.lineEditOrder.sizePolicy().hasHeightForWidth())
        self.lineEditOrder.setSizePolicy(sizePolicy2)
        self.lineEditOrder.setMinimumSize(QSize(0, 21))
        self.lineEditOrder.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditOrder.setStyleSheet(u"")
        self.lineEditOrder.setAlignment(Qt.AlignCenter)
        self.lineEditOrder.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditOrder, 4, 1, 1, 1)

        self.label_6 = QLabel(widgetRoot)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEditFamily = QLineEdit(widgetRoot)
        self.lineEditFamily.setObjectName(u"lineEditFamily")
        sizePolicy2.setHeightForWidth(self.lineEditFamily.sizePolicy().hasHeightForWidth())
        self.lineEditFamily.setSizePolicy(sizePolicy2)
        self.lineEditFamily.setMinimumSize(QSize(0, 21))
        self.lineEditFamily.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditFamily.setStyleSheet(u"")
        self.lineEditFamily.setAlignment(Qt.AlignCenter)
        self.lineEditFamily.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditFamily, 5, 1, 1, 1)

        self.label_7 = QLabel(widgetRoot)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.lineEditGenus = QLineEdit(widgetRoot)
        self.lineEditGenus.setObjectName(u"lineEditGenus")
        sizePolicy2.setHeightForWidth(self.lineEditGenus.sizePolicy().hasHeightForWidth())
        self.lineEditGenus.setSizePolicy(sizePolicy2)
        self.lineEditGenus.setMinimumSize(QSize(0, 21))
        self.lineEditGenus.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditGenus.setStyleSheet(u"")
        self.lineEditGenus.setAlignment(Qt.AlignCenter)
        self.lineEditGenus.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditGenus, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButtonInsert = QPushButton(widgetRoot)
        self.pushButtonInsert.setObjectName(u"pushButtonInsert")
        sizePolicy2.setHeightForWidth(self.pushButtonInsert.sizePolicy().hasHeightForWidth())
        self.pushButtonInsert.setSizePolicy(sizePolicy2)
        self.pushButtonInsert.setMinimumSize(QSize(0, 23))

        self.verticalLayout.addWidget(self.pushButtonInsert)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButtonDB = QPushButton(widgetRoot)
        self.pushButtonDB.setObjectName(u"pushButtonDB")
        sizePolicy2.setHeightForWidth(self.pushButtonDB.sizePolicy().hasHeightForWidth())
        self.pushButtonDB.setSizePolicy(sizePolicy2)
        self.pushButtonDB.setMinimumSize(QSize(0, 23))
        self.pushButtonDB.setMaximumSize(QSize(16777215, 16777215))
        self.pushButtonDB.setAutoDefault(False)
        self.pushButtonDB.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButtonDB)

        self.pushButtonWoRMS = QPushButton(widgetRoot)
        self.pushButtonWoRMS.setObjectName(u"pushButtonWoRMS")
        sizePolicy2.setHeightForWidth(self.pushButtonWoRMS.sizePolicy().hasHeightForWidth())
        self.pushButtonWoRMS.setSizePolicy(sizePolicy2)
        self.pushButtonWoRMS.setMinimumSize(QSize(0, 23))
        self.pushButtonWoRMS.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButtonWoRMS)

        self.pushButtonGBIF = QPushButton(widgetRoot)
        self.pushButtonGBIF.setObjectName(u"pushButtonGBIF")
        sizePolicy2.setHeightForWidth(self.pushButtonGBIF.sizePolicy().hasHeightForWidth())
        self.pushButtonGBIF.setSizePolicy(sizePolicy2)
        self.pushButtonGBIF.setMinimumSize(QSize(0, 23))
        self.pushButtonGBIF.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButtonGBIF)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(2, 1)
        QWidget.setTabOrder(self.lineEditSpecies, self.lineEditKingdom)
        QWidget.setTabOrder(self.lineEditKingdom, self.lineEditPhylum)
        QWidget.setTabOrder(self.lineEditPhylum, self.lineEditClass)
        QWidget.setTabOrder(self.lineEditClass, self.lineEditOrder)
        QWidget.setTabOrder(self.lineEditOrder, self.lineEditFamily)
        QWidget.setTabOrder(self.lineEditFamily, self.lineEditGenus)
        QWidget.setTabOrder(self.lineEditGenus, self.pushButtonInsert)
        QWidget.setTabOrder(self.pushButtonInsert, self.pushButtonWoRMS)
        QWidget.setTabOrder(self.pushButtonWoRMS, self.pushButtonGBIF)

        self.retranslateUi(widgetRoot)

        self.pushButtonDB.setDefault(False)


        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.label.setText(QCoreApplication.translate("widgetRoot", u"Species", None))
        self.label_2.setText(QCoreApplication.translate("widgetRoot", u"Kingdom", None))
        self.label_3.setText(QCoreApplication.translate("widgetRoot", u"Phylum", None))
        self.label_5.setText(QCoreApplication.translate("widgetRoot", u"Class", None))
        self.label_4.setText(QCoreApplication.translate("widgetRoot", u"Order", None))
        self.label_6.setText(QCoreApplication.translate("widgetRoot", u"Family", None))
        self.label_7.setText(QCoreApplication.translate("widgetRoot", u"Genus", None))
        self.pushButtonInsert.setText(QCoreApplication.translate("widgetRoot", u"Insert", None))
        self.pushButtonDB.setText(QCoreApplication.translate("widgetRoot", u"DB", None))
        self.pushButtonWoRMS.setText(QCoreApplication.translate("widgetRoot", u"WoRMS", None))
        self.pushButtonGBIF.setText(QCoreApplication.translate("widgetRoot", u"GBIF", None))
    # retranslateUi

