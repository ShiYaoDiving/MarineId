# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetGalleryItem.ui'
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

        self.labelCommonName = QLabel(widgetRoot)
        self.labelCommonName.setObjectName(u"labelCommonName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelCommonName.sizePolicy().hasHeightForWidth())
        self.labelCommonName.setSizePolicy(sizePolicy1)
        self.labelCommonName.setMinimumSize(QSize(0, 15))
        self.labelCommonName.setMaximumSize(QSize(16777215, 15))
        font = QFont()
        font.setBold(True)
        self.labelCommonName.setFont(font)
        self.labelCommonName.setStyleSheet(u"background-color: rgb(220, 220, 220); color: black;")
        self.labelCommonName.setFrameShape(QFrame.NoFrame)
        self.labelCommonName.setFrameShadow(QFrame.Plain)
        self.labelCommonName.setScaledContents(True)
        self.labelCommonName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelCommonName)

        self.labelName = QLabel(widgetRoot)
        self.labelName.setObjectName(u"labelName")
        sizePolicy1.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy1)
        self.labelName.setMinimumSize(QSize(0, 15))
        self.labelName.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(True)
        self.labelName.setFont(font1)
        self.labelName.setStyleSheet(u"background-color: rgb(220, 220, 220); color: black;")
        self.labelName.setFrameShape(QFrame.NoFrame)
        self.labelName.setFrameShadow(QFrame.Plain)
        self.labelName.setScaledContents(True)
        self.labelName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelName)


        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.labelPic.setText(QCoreApplication.translate("widgetRoot", u"No Picture", None))
        self.labelCommonName.setText(QCoreApplication.translate("widgetRoot", u"\u5df4\u6c0f\u8c46\u4e01\u6d77\u9a6c", None))
        self.labelName.setText(QCoreApplication.translate("widgetRoot", u"Hippocampus bargibanti", None))
    # retranslateUi

