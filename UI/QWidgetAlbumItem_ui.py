# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetAlbumItem.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.resize(200, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(widgetRoot)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelPic = QLabel(widgetRoot)
        self.labelPic.setObjectName(u"labelPic")
        sizePolicy.setHeightForWidth(self.labelPic.sizePolicy().hasHeightForWidth())
        self.labelPic.setSizePolicy(sizePolicy)
        self.labelPic.setMinimumSize(QSize(0, 0))
        self.labelPic.setMaximumSize(QSize(16777215, 16777215))
        self.labelPic.setStyleSheet(u"background-color: rgb(250, 250, 250); color: Red;")
        self.labelPic.setFrameShape(QFrame.NoFrame)
        self.labelPic.setFrameShadow(QFrame.Plain)
        self.labelPic.setMidLineWidth(0)
        self.labelPic.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelPic)

        self.labelDatetime = QLabel(widgetRoot)
        self.labelDatetime.setObjectName(u"labelDatetime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelDatetime.sizePolicy().hasHeightForWidth())
        self.labelDatetime.setSizePolicy(sizePolicy1)
        self.labelDatetime.setMinimumSize(QSize(0, 15))
        self.labelDatetime.setMaximumSize(QSize(16777215, 15))
        font = QFont()
        font.setBold(True)
        self.labelDatetime.setFont(font)
        self.labelDatetime.setStyleSheet(u"background-color: rgb(220, 220, 220); color: black;")
        self.labelDatetime.setFrameShape(QFrame.NoFrame)
        self.labelDatetime.setFrameShadow(QFrame.Plain)
        self.labelDatetime.setScaledContents(True)
        self.labelDatetime.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelDatetime)

        self.labelDiveSite = QLabel(widgetRoot)
        self.labelDiveSite.setObjectName(u"labelDiveSite")
        sizePolicy1.setHeightForWidth(self.labelDiveSite.sizePolicy().hasHeightForWidth())
        self.labelDiveSite.setSizePolicy(sizePolicy1)
        self.labelDiveSite.setMinimumSize(QSize(0, 15))
        self.labelDiveSite.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(True)
        self.labelDiveSite.setFont(font1)
        self.labelDiveSite.setStyleSheet(u"background-color: rgb(220, 220, 220); color: black;")
        self.labelDiveSite.setFrameShape(QFrame.NoFrame)
        self.labelDiveSite.setFrameShadow(QFrame.Plain)
        self.labelDiveSite.setScaledContents(True)
        self.labelDiveSite.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelDiveSite)


        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.labelPic.setText(QCoreApplication.translate("widgetRoot", u"No Picture", None))
        self.labelDatetime.setText(QCoreApplication.translate("widgetRoot", u"1990-10-01 12:11:44", None))
        self.labelDiveSite.setText(QCoreApplication.translate("widgetRoot", u"Ambon ,Laha 2", None))
    # retranslateUi

