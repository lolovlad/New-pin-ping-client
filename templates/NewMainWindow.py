# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 790)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 621, 811))
        self.frame.setStyleSheet(u"background: rgb(0, 0, 0);\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 621, 101))
        font = QFont()
        font.setPointSize(43)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(120, 130, 381, 102))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_nickname = QLabel(self.horizontalLayoutWidget)
        self.label_nickname.setObjectName(u"label_nickname")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_nickname.setFont(font1)
        self.label_nickname.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_nickname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_nickname)

        self.button_edit_nickname = QPushButton(self.horizontalLayoutWidget)
        self.button_edit_nickname.setObjectName(u"button_edit_nickname")
        self.button_edit_nickname.setEnabled(True)
        self.button_edit_nickname.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.button_edit_nickname.setFont(font2)
        self.button_edit_nickname.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;")

        self.horizontalLayout_2.addWidget(self.button_edit_nickname)

        self.horizontalLayoutWidget_2 = QWidget(self.frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(50, 250, 531, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_game_mode = QLabel(self.horizontalLayoutWidget_2)
        self.label_game_mode.setObjectName(u"label_game_mode")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_game_mode.setFont(font3)
        self.label_game_mode.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_game_mode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_game_mode)

        self.button_vs_player = QPushButton(self.horizontalLayoutWidget_2)
        self.button_vs_player.setObjectName(u"button_vs_player")
        self.button_vs_player.setEnabled(True)
        self.button_vs_player.setMinimumSize(QSize(100, 40))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.button_vs_player.setFont(font4)
        self.button_vs_player.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;")

        self.horizontalLayout_3.addWidget(self.button_vs_player)

        self.button_vs_bot = QPushButton(self.horizontalLayoutWidget_2)
        self.button_vs_bot.setObjectName(u"button_vs_bot")
        self.button_vs_bot.setEnabled(True)
        self.button_vs_bot.setMinimumSize(QSize(100, 40))
        self.button_vs_bot.setFont(font4)
        self.button_vs_bot.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;")

        self.horizontalLayout_3.addWidget(self.button_vs_bot)

        self.horizontalLayoutWidget_3 = QWidget(self.frame)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(50, 360, 531, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setSpacing(11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.button_edit_skin_player = QPushButton(self.horizontalLayoutWidget_3)
        self.button_edit_skin_player.setObjectName(u"button_edit_skin_player")
        self.button_edit_skin_player.setEnabled(True)
        self.button_edit_skin_player.setMinimumSize(QSize(100, 40))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.button_edit_skin_player.setFont(font6)
        self.button_edit_skin_player.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;")

        self.horizontalLayout_4.addWidget(self.button_edit_skin_player)

        self.label_view_skin_player = QLabel(self.horizontalLayoutWidget_3)
        self.label_view_skin_player.setObjectName(u"label_view_skin_player")
        self.label_view_skin_player.setStyleSheet(u"background-color: rgb(170, 85, 255);")

        self.horizontalLayout_4.addWidget(self.label_view_skin_player)

        self.horizontalLayoutWidget_4 = QWidget(self.frame)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(50, 480, 531, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setSpacing(11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.button_edit_skin_field = QPushButton(self.horizontalLayoutWidget_4)
        self.button_edit_skin_field.setObjectName(u"button_edit_skin_field")
        self.button_edit_skin_field.setEnabled(True)
        self.button_edit_skin_field.setMinimumSize(QSize(100, 40))
        self.button_edit_skin_field.setFont(font6)
        self.button_edit_skin_field.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;")

        self.horizontalLayout_5.addWidget(self.button_edit_skin_field)

        self.label_view_skin_field = QLabel(self.horizontalLayoutWidget_4)
        self.label_view_skin_field.setObjectName(u"label_view_skin_field")
        self.label_view_skin_field.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_view_skin_field)

        self.button_start_search = QPushButton(self.frame)
        self.button_start_search.setObjectName(u"button_start_search")
        self.button_start_search.setEnabled(True)
        self.button_start_search.setGeometry(QRect(190, 600, 261, 40))
        self.button_start_search.setMinimumSize(QSize(100, 40))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.button_start_search.setFont(font7)
        self.button_start_search.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;")
        self.butto_settings = QPushButton(self.frame)
        self.butto_settings.setObjectName(u"butto_settings")
        self.butto_settings.setEnabled(True)
        self.butto_settings.setGeometry(QRect(520, 670, 94, 91))
        self.butto_settings.setMinimumSize(QSize(94, 38))
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        self.butto_settings.setFont(font8)
        self.butto_settings.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border:none;\n"
"image: url(./File/263074.png);\n"
"padding: 5;")
        self.table_leaderboard = QTableWidget(self.centralwidget)
        if (self.table_leaderboard.columnCount() < 4):
            self.table_leaderboard.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_leaderboard.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_leaderboard.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_leaderboard.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_leaderboard.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_leaderboard.rowCount() < 1):
            self.table_leaderboard.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_leaderboard.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_leaderboard.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_leaderboard.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_leaderboard.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_leaderboard.setItem(0, 3, __qtablewidgetitem8)
        self.table_leaderboard.setObjectName(u"table_leaderboard")
        self.table_leaderboard.setGeometry(QRect(630, 90, 561, 321))
        self.table_leaderboard.horizontalHeader().setCascadingSectionResizes(True)
        self.table_leaderboard.horizontalHeader().setDefaultSectionSize(129)
        self.table_leaderboard.horizontalHeader().setStretchLastSection(True)
        self.table_leaderboard.verticalHeader().setCascadingSectionResizes(False)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(630, 0, 561, 91))
        font9 = QFont()
        font9.setPointSize(22)
        font9.setBold(True)
        self.label_8.setFont(font9)
        self.label_8.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(630, 420, 561, 61))
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_view_mmr = QLabel(self.centralwidget)
        self.label_view_mmr.setObjectName(u"label_view_mmr")
        self.label_view_mmr.setGeometry(QRect(630, 480, 561, 81))
        self.label_view_mmr.setFont(font9)
        self.label_view_mmr.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_view_mmr.setAlignment(Qt.AlignCenter)
        self.label_icon_mmr = QLabel(self.centralwidget)
        self.label_icon_mmr.setObjectName(u"label_icon_mmr")
        self.label_icon_mmr.setGeometry(QRect(780, 550, 251, 211))
        self.label_icon_mmr.setFont(font9)
        self.label_icon_mmr.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"background-image: url(./File/SeasonalRank3-4.png);")
        self.label_icon_mmr.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PIN-PONG 2.V", None))
        self.label_nickname.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.button_edit_nickname.setText(QCoreApplication.translate("MainWindow", u"\u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0438\u043a\u043d\u0435\u0439\u043c", None))
        self.label_game_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0438\u0433\u0440\u044b: \u041f\u0440\u043e\u0442\u0438\u0432 \u0438\u0433\u0440\u043e\u043a\u043e\u0432", None))
        self.button_vs_player.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u0438\u0432 \u0438\u0433\u0440\u043e\u043a\u043e\u0432", None))
        self.button_vs_bot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u0438\u0432 \u0431\u043e\u0442\u043e\u0432", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u0441\u043a\u0438\u043d \u0434\u043b\u044f \u0438\u0433\u0440\u044b", None))
        self.button_edit_skin_player.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u043a\u0438\u043d\u0430", None))
        self.label_view_skin_player.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u0444\u043e\u043d \u0438\u0433\u0440\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044f", None))
        self.button_edit_skin_field.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u043e\u043d", None))
        self.label_view_skin_field.setText("")
        self.button_start_search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043f\u043e\u0438\u0441\u043a", None))
        self.butto_settings.setText("")
        ___qtablewidgetitem = self.table_leaderboard.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a\u043d\u0435\u0439\u043c", None));
        ___qtablewidgetitem1 = self.table_leaderboard.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u043d\u0433", None));
        ___qtablewidgetitem2 = self.table_leaderboard.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0440\u0440", None));
        ___qtablewidgetitem3 = self.table_leaderboard.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043d\u0440\u0435\u0439\u0442 %", None));
        ___qtablewidgetitem4 = self.table_leaderboard.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"0", None));

        __sortingEnabled = self.table_leaderboard.isSortingEnabled()
        self.table_leaderboard.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.table_leaderboard.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"kek", None));
        ___qtablewidgetitem6 = self.table_leaderboard.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0441\u0442\u0435\u043b\u0438\u043d", None));
        ___qtablewidgetitem7 = self.table_leaderboard.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4500", None));
        ___qtablewidgetitem8 = self.table_leaderboard.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"60", None));
        self.table_leaderboard.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043b\u0438\u0434\u0435\u0440\u043e\u0432", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 \u0440\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.label_view_mmr.setText(QCoreApplication.translate("MainWindow", u"1000 \u043c\u043c\u0440", None))
        self.label_icon_mmr.setText("")
    # retranslateUi

