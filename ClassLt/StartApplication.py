from Interfase import Singleton
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as orm
from Class.SqliteContext import SqliteContext


class StartApplication(metaclass=Singleton):
    __model = declarative_base()
    __context = None

    @property
    def context(self):
        return self.__context

    def __create_context(self):
        name_database = SqliteContext().create_context()

        engine = create_engine(name_database, echo=True)
        self.__context = orm.sessionmaker(bind=engine)()
        self.__model.metadata.create_all(engine)

    def context_validation_and_creation(self):
        try:
            self.__create_context()
        except Exception:
            self.__create_context()

    @property
    def model(self):
        return self.__model
