# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_History(object):
    def setupUi(self, History):
        if not History.objectName():
            History.setObjectName(u"History")
        History.resize(400, 292)
        self.gridLayout_2 = QGridLayout(History)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nums = QLabel(History)
        self.nums.setObjectName(u"nums")

        self.horizontalLayout.addWidget(self.nums)

        self.pages = QLabel(History)
        self.pages.setObjectName(u"pages")

        self.horizontalLayout.addWidget(self.pages)

        self.lineEdit = QLineEdit(History)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.jumpButton = QPushButton(History)
        self.jumpButton.setObjectName(u"jumpButton")

        self.horizontalLayout.addWidget(self.jumpButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.retranslateUi(History)
        self.jumpButton.clicked.connect(History.JumpPage)

        QMetaObject.connectSlotsByName(History)
    # setupUi

    def retranslateUi(self, History):
        History.setWindowTitle(QCoreApplication.translate("History", u"Form", None))
        self.nums.setText(QCoreApplication.translate("History", u"\u6536\u85cf\u6570\uff1a", None))
        self.pages.setText(QCoreApplication.translate("History", u"\u9875", None))
        self.jumpButton.setText(QCoreApplication.translate("History", u"\u8df3\u8f6c", None))
#if QT_CONFIG(shortcut)
        self.jumpButton.setShortcut(QCoreApplication.translate("History", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

