from Interfase import Subject


class DialogSelectSkinModel(Subject):
    def __init__(self):
        self.__observers = []

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for i in self.__observers:
            i.update()

    def attach(self, observer):
        self.__observers.append(observer)