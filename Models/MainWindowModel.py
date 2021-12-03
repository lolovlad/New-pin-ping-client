from Interfase import Subject


class MainWindowModel(Subject):
    def __init__(self):
        self.__state = ""

        self.__observers = []

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, val):
        self.__state = val
        self.notify()

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for i in self.__observers:
            i.update()

    def attach(self, observer):
        self.__observers.append(observer)