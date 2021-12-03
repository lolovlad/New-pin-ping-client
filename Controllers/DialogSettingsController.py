import sys
from PySide6.QtWidgets import QApplication
from ClassLt.Session import Session
from Views.DialogSettingsView import DialogSettingsView


class DialogSettingsController:

    def __init__(self, model):
        self.__model = model
        self.__view = DialogSettingsView(self, self.__model)
        self.__view.show()