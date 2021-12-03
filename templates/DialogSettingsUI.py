# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DialogSettings(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 452)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 80, 421, 101))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 211, 51))
        font = QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 200, 211, 51))
        self.label_5.setFont(font)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 270, 421, 101))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_11)

        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_12)

        self.label_13 = QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_13)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 390, 91, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 390, 171, 24))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 390, 101, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0440\u0430\u043a\u0435\u0442\u043a\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0438\u0432 \u0431\u043e\u0442\u043e\u0432:", None))
        self.label_3.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u043a\u0430\u044f", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u0430\u044f", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0432\u0432\u0435\u0440\u0445:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0432\u043d\u0438\u0437", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u044c\u043d\u044b\u0439 \u0443\u0434\u0430\u0440", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043a\u043e\u0440\u0435\u043d\u0438\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e \u0443\u043c\u0430\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

