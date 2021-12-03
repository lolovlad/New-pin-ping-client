# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(861, 578)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 891, 131))
        self.frame.setStyleSheet(u"background-color:rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 19, 841, 101))
        font = QFont()
        font.setFamilies([u"Lucida Bright"])
        font.setPointSize(31)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.sigin_button = QPushButton(self.centralwidget)
        self.sigin_button.setObjectName(u"sigin_button")
        self.sigin_button.setGeometry(QRect(300, 360, 241, 24))
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(220, 425, 411, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.error_label.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(220, 230, 411, 111))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMargin(11)

        self.horizontalLayout.addWidget(self.label)

        self.email_edit = QLineEdit(self.layoutWidget)
        self.email_edit.setObjectName(u"email_edit")

        self.horizontalLayout.addWidget(self.email_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.password_edit = QLineEdit(self.layoutWidget)
        self.password_edit.setObjectName(u"password_edit")

        self.horizontalLayout_2.addWidget(self.password_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"login", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"PIN-PONG 2.V", None))
        self.sigin_button.setText(QCoreApplication.translate("LoginWindow", u"sigin", None))
        self.error_label.setText("")
        self.label.setText(QCoreApplication.translate("LoginWindow", u"email", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"password", None))
    # retranslateUi

