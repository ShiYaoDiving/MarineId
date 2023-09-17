# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetGallery.ui'
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
    QHBoxLayout, QLabel, QLayout, QScrollArea,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.setWindowModality(Qt.NonModal)
        widgetRoot.resize(300, 338)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        widgetRoot.setMinimumSize(QSize(300, 0))
        widgetRoot.setAcceptDrops(True)
        widgetRoot.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(widgetRoot)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelName = QLabel(widgetRoot)
        self.labelName.setObjectName(u"labelName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy1)
        self.labelName.setMinimumSize(QSize(0, 25))
        self.labelName.setMaximumSize(QSize(16777215, 22))
        font = QFont()
        font.setPointSize(15)
        self.labelName.setFont(font)

        self.verticalLayout.addWidget(self.labelName)

        self.labelAlbumNumber = QLabel(widgetRoot)
        self.labelAlbumNumber.setObjectName(u"labelAlbumNumber")

        self.verticalLayout.addWidget(self.labelAlbumNumber)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sliderSize = QSlider(widgetRoot)
        self.sliderSize.setObjectName(u"sliderSize")
        self.sliderSize.setMinimumSize(QSize(150, 22))
        self.sliderSize.setMaximumSize(QSize(150, 22))
        self.sliderSize.setMinimum(100)
        self.sliderSize.setMaximum(600)
        self.sliderSize.setValue(300)
        self.sliderSize.setOrientation(Qt.Horizontal)
        self.sliderSize.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout.addWidget(self.sliderSize)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.setStretch(0, 1)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 263, 266))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(50, 0))
        self.scrollAreaWidgetContents.setAcceptDrops(True)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
        self.labelName.setText(QCoreApplication.translate("widgetRoot", u"Gallery", None))
        self.labelAlbumNumber.setText(QCoreApplication.translate("widgetRoot", u"0 Albums", None))
    # retranslateUi

