from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from templates.LoginUI import Ui_LoginWindow
from Interfase import Observer


class LoginView(QMainWindow):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super().__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_LoginWindow()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        self.__ui.email_edit.editingFinished.connect(self.__controller.set_mail)
        self.__ui.password_edit.editingFinished.connect(self.__controller.set_password)

        self.__ui.sigin_button.clicked.connect(self.__controller.login)

    @property
    def ui(self):
        return self.__ui

    def update(self):
        self.__ui.error_label.setText(self.__model.error)



