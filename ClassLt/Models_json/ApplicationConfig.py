from pykson import JsonObject, ObjectField
from ClassLt.Models_json import Server, DataBase, Socket


class ApplicationConfig(JsonObject):
    server = ObjectField(Server)
    data_base = ObjectField(DataBase)
    socket = ObjectField(Socket)
