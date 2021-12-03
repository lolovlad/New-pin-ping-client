# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Launcher.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Launcher(object):
    def setupUi(self, Launcher):
        if not Launcher.objectName():
            Launcher.setObjectName(u"Launcher")
        Launcher.resize(1009, 593)
        font = QFont()
        font.setPointSize(12)
        Launcher.setFont(font)
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(930, 0, 75, 71))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 180, 261, 61))
        font1 = QFont()
        font1.setPointSize(23)
        self.label.setFont(font1)
        self.state_label = QLabel(self.centralwidget)
        self.state_label.setObjectName(u"state_label")
        self.state_label.setGeometry(QRect(370, 440, 261, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(370, 250, 261, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.start_game_button = QPushButton(self.widget)
        self.start_game_button.setObjectName(u"start_game_button")

        self.verticalLayout.addWidget(self.start_game_button)

        self.settings_button = QPushButton(self.widget)
        self.settings_button.setObjectName(u"settings_button")

        self.verticalLayout.addWidget(self.settings_button)

        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Launcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1009, 28))
        Launcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Launcher)
        self.statusbar.setObjectName(u"statusbar")
        Launcher.setStatusBar(self.statusbar)

        self.retranslateUi(Launcher)

        QMetaObject.connectSlotsByName(Launcher)
    # setupUi

    def retranslateUi(self, Launcher):
        Launcher.setWindowTitle(QCoreApplication.translate("Launcher", u"Launcher", None))
        self.close_button.setText(QCoreApplication.translate("Launcher", u"X", None))
        self.label.setText(QCoreApplication.translate("Launcher", u"Pin-pong 2.0V", None))
        self.state_label.setText("")
        self.start_game_button.setText(QCoreApplication.translate("Launcher", u"StartGame", None))
        self.settings_button.setText(QCoreApplication.translate("Launcher", u"settings", None))
    # retranslateUi

