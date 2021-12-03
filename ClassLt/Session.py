from Interfase import Singleton


class Session(metaclass=Singleton):
    __session = None

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, user):
        self.__session = user