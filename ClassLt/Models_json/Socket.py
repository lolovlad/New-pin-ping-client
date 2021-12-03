from pykson import IntegerField, StringField, JsonObject


class Socket(JsonObject):
    ip = StringField()
    port = IntegerField()