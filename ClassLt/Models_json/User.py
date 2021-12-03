from pykson import JsonObject, StringField, IntegerField


class User(JsonObject):
    id = IntegerField()
    email = StringField()
    nickname = StringField()
    password = StringField()