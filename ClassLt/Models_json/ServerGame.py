from pykson import JsonObject, StringField, IntegerField


class ServerGame(JsonObject):
    ip = StringField()
    port = IntegerField()