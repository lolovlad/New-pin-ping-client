from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from templates.NewMainWindow import Ui_MainWindow
from Interfase import Observer


class NewMainWindowView(QMainWindow):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super().__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.button_edit_skin_player.clicked.connect(self.__controller.edit_select_skin)
        self.__ui.butto_settings.clicked.connect(self.__controller.edit_settings)

        self.__model.attach(self)

    @property
    def ui(self):
        return self.__ui

    def update(self):
        pass
