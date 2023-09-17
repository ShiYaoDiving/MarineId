# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetAlbum.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPlainTextEdit,
    QScrollArea, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.setWindowModality(Qt.NonModal)
        widgetRoot.resize(400, 572)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        widgetRoot.setMinimumSize(QSize(400, 0))
        widgetRoot.setAcceptDrops(True)
        widgetRoot.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(widgetRoot)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.labelThumb = QLabel(widgetRoot)
        self.labelThumb.setObjectName(u"labelThumb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelThumb.sizePolicy().hasHeightForWidth())
        self.labelThumb.setSizePolicy(sizePolicy1)
        self.labelThumb.setMinimumSize(QSize(150, 150))
        self.labelThumb.setMaximumSize(QSize(150, 150))
        self.labelThumb.setStyleSheet(u"background-color:white;")
        self.labelThumb.setFrameShape(QFrame.Box)
        self.labelThumb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelThumb)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelName = QLabel(widgetRoot)
        self.labelName.setObjectName(u"labelName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy2)
        self.labelName.setMinimumSize(QSize(0, 25))
        self.labelName.setMaximumSize(QSize(16777215, 22))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setKerning(True)
        self.labelName.setFont(font)

        self.verticalLayout.addWidget(self.labelName)

        self.labelCommon = QLabel(widgetRoot)
        self.labelCommon.setObjectName(u"labelCommon")
        font1 = QFont()
        font1.setBold(True)
        self.labelCommon.setFont(font1)

        self.verticalLayout.addWidget(self.labelCommon)

        self.labelOther = QLabel(widgetRoot)
        self.labelOther.setObjectName(u"labelOther")
        font2 = QFont()
        font2.setBold(False)
        self.labelOther.setFont(font2)

        self.verticalLayout.addWidget(self.labelOther)

        self.plainTextEditInfomation = QPlainTextEdit(widgetRoot)
        self.plainTextEditInfomation.setObjectName(u"plainTextEditInfomation")
        self.plainTextEditInfomation.setMinimumSize(QSize(0, 0))
        self.plainTextEditInfomation.setMaximumSize(QSize(16777215, 80))
        self.plainTextEditInfomation.setStyleSheet(u"background-color:rgb(240, 240, 240);")
        self.plainTextEditInfomation.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.plainTextEditInfomation.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEditInfomation)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sliderSize = QSlider(widgetRoot)
        self.sliderSize.setObjectName(u"sliderSize")
        self.sliderSize.setMinimumSize(QSize(22, 150))
        self.sliderSize.setMaximumSize(QSize(22, 150))
        self.sliderSize.setMinimum(200)
        self.sliderSize.setMaximum(600)
        self.sliderSize.setValue(350)
        self.sliderSize.setOrientation(Qt.Vertical)
        self.sliderSize.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout.addWidget(self.sliderSize)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(widgetRoot)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 363, 392))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(50, 0))
        self.scrollAreaWidgetContents.setAcceptDrops(True)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.labelThumb.setText(QCoreApplication.translate("widgetRoot", u"Thumb", None))
        self.labelName.setText(QCoreApplication.translate("widgetRoot", u"Scientific Name", None))
        self.labelCommon.setText(QCoreApplication.translate("widgetRoot", u"Common Name", None))
        self.labelOther.setText(QCoreApplication.translate("widgetRoot", u"Other Names", None))
    # retranslateUi

