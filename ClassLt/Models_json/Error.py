from pykson import JsonObject, StringField


class Error(JsonObject):
    type_error = StringField()
    massage_error = StringField()
