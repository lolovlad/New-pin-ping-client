import sys
from PySide6.QtWidgets import QApplication
from ClassLt.Session import Session
from Views.NewMainWindowView import NewMainWindowView

from Models.DialogSelectSkinModel import DialogSelectSkinModel
from Controllers.DialogSelectSkinController import DialogSelectSkinController

from Models.DialogSettingsModel import DialogSettingsModel
from Controllers.DialogSettingsController import DialogSettingsController


class NewMainWindowController:

    def __init__(self, model):
        self.__model = model
        self.__view = NewMainWindowView(self, self.__model)
        self.__view.show()

    def edit_select_skin(self):
        model = DialogSelectSkinModel()
        controller = DialogSelectSkinController(model)

    def edit_settings(self):
        model = DialogSettingsModel()
        controller = DialogSettingsController(model)