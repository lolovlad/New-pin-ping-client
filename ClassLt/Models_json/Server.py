from pykson import JsonObject, StringField


class Server(JsonObject):
    key = StringField()
    url = StringField()
