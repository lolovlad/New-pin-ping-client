import sys
from PySide6.QtWidgets import QApplication
from ClassLt.ServerRespons import ServerResponse
from ClassLt.Session import Session
from Views import LoginView
from Models.MainWindowModel import MainWindowModel
from Controllers.MainWindowController import MainWindowController

from Models.NewMainWindowModel import NewMainWindowModel
from Controllers.NewMainWindowController import NewMainWindowController


class LoginController:

    def __init__(self, model):
        self.__model = model
        self.__view = LoginView(self, self.__model)
        self.__view.show()

    def set_mail(self):
        mail = self.__view.ui.email_edit.text()
        self.__model.mail = mail

    def set_password(self):
        password = self.__view.ui.password_edit.text()
        self.__model.password = password

    def login(self):
        request = {"email": self.__model.mail, "password": self.__model.password,
                   "type_request": "login"}
        is_login, response = ServerResponse.check_entry_account(request)
        if is_login:
            model = NewMainWindowModel()
            Session().session = response
            controller = NewMainWindowController(model)
            self.__view.close()
        else:
            self.__model.error = response

