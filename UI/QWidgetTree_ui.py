# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetTree.ui'
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
    QHeaderView, QLayout, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_widgetRoot(object):
    def setupUi(self, widgetRoot):
        if not widgetRoot.objectName():
            widgetRoot.setObjectName(u"widgetRoot")
        widgetRoot.resize(247, 544)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetRoot.sizePolicy().hasHeightForWidth())
        widgetRoot.setSizePolicy(sizePolicy)
        widgetRoot.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(widgetRoot)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.treeWidgetTaxonomic = QTreeWidget(widgetRoot)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidgetTaxonomic.setHeaderItem(__qtreewidgetitem)
        self.treeWidgetTaxonomic.setObjectName(u"treeWidgetTaxonomic")
        self.treeWidgetTaxonomic.setMinimumSize(QSize(0, 0))
        self.treeWidgetTaxonomic.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.treeWidgetTaxonomic.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeWidgetTaxonomic.setIndentation(10)
        self.treeWidgetTaxonomic.header().setVisible(False)
        self.treeWidgetTaxonomic.header().setMinimumSectionSize(100)
        self.treeWidgetTaxonomic.header().setDefaultSectionSize(100)

        self.gridLayout.addWidget(self.treeWidgetTaxonomic, 0, 0, 1, 1)


        self.retranslateUi(widgetRoot)

        QMetaObject.connectSlotsByName(widgetRoot)
    # setupUi

    def retranslateUi(self, widgetRoot):
        widgetRoot.setWindowTitle(QCoreApplication.translate("widgetRoot", u"Form", None))
    # retranslateUi

