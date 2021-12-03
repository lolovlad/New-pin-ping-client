from PySide6.QtWidgets import QMainWindow
from templates.MainWindowUI import Ui_Launcher
from Interfase import Observer


class MainWindowView(QMainWindow):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super().__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_Launcher()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        self.__ui.start_game_button.clicked.connect(self.__controller.start_search_game)

    @property
    def ui(self):
        return self.__ui

    def update(self):
        self.__ui.state_label.setText(self.__model.state)


