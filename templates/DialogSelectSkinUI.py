# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogSelectSkin.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_DialogEditSkin(object):
    def setupUi(self, DialogEditSkin):
        if not DialogEditSkin.objectName():
            DialogEditSkin.setObjectName(u"DialogEditSkin")
        DialogEditSkin.resize(400, 390)
        font = QFont()
        font.setPointSize(9)
        DialogEditSkin.setFont(font)
        self.buttonBox = QDialogButtonBox(DialogEditSkin)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 350, 371, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.list_skin = QListWidget(DialogEditSkin)
        QListWidgetItem(self.list_skin)
        self.list_skin.setObjectName(u"list_skin")
        self.list_skin.setGeometry(QRect(10, 10, 111, 321))
        font1 = QFont()
        font1.setPointSize(17)
        self.list_skin.setFont(font1)
        self.label_skin_view = QLabel(DialogEditSkin)
        self.label_skin_view.setObjectName(u"label_skin_view")
        self.label_skin_view.setGeometry(QRect(160, 60, 201, 211))
        self.label_skin_view.setStyleSheet(u"background-color: rgb(170, 85, 255);")

        self.retranslateUi(DialogEditSkin)
        self.buttonBox.accepted.connect(DialogEditSkin.accept)
        self.buttonBox.rejected.connect(DialogEditSkin.reject)

        QMetaObject.connectSlotsByName(DialogEditSkin)
    # setupUi

    def retranslateUi(self, DialogEditSkin):
        DialogEditSkin.setWindowTitle(QCoreApplication.translate("DialogEditSkin", u"Dialog", None))

        __sortingEnabled = self.list_skin.isSortingEnabled()
        self.list_skin.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_skin.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("DialogEditSkin", u"nitro", None));
        self.list_skin.setSortingEnabled(__sortingEnabled)

        self.label_skin_view.setText("")
    # retranslateUi

