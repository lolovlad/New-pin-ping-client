import sys
from PySide6.QtWidgets import QApplication
from ClassLt.Session import Session
from Views.DialogSelectSkinView import DialogSelectSkinView


class DialogSelectSkinController:

    def __init__(self, model):
        self.__model = model
        self.__view = DialogSelectSkinView(self, self.__model)
        self.__view.show()
        self.__view.exec()