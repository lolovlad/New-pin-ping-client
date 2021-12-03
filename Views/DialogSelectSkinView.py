from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6 import QtWidgets
from templates.DialogSelectSkinUI import Ui_DialogEditSkin
from Interfase import Observer


class DialogSelectSkinView(QDialog):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super().__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_DialogEditSkin()
        self.__ui.setupUi(self)

        self.__model.attach(self)

    @property
    def ui(self):
        return self.__ui

    def update(self):
        pass