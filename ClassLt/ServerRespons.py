from Core.Network import NetWork
from pykson import Pykson
from ClassLt.Models_json import User, Error
from ClassLt.Сonfiguration import Configuration


class ServerResponse:
    config_socket = Configuration("ApplicationConfiguration").load().socket
    socket = NetWork()
    socket(config_socket.ip, config_socket.port)

    @classmethod
    def __network_core(cls, message):
        cls.socket.send_message(message)
        while True:
            command = cls.socket.listener()
            if command["type_request"] == "login":
                return command
            elif command["type_request"] == "add_list":
                return command
            elif command["type_request"] == "registration":
                return command

    @staticmethod
    def __serialized_object(response, model):
        if response["type_request"]:
            json_model = Pykson().from_json(response["response"], model)
            return json_model
        else:
            error = Pykson().from_json(response["response"], Error)
            raise type(error.type_error, (Exception,), {})(error.massage_error)

    @classmethod
    def __json_request(cls, request):
        url = cls.socket.send_message(request)
        return url

    @classmethod
    def __account_request(cls, request):
        json_request = cls.__network_core(request)
        return cls.__serialized_object(json_request, User)

    @classmethod
    def __registration_account_request(cls, request):
        json_request = cls.__network_core(request)
        return cls.__serialized_object(json_request, User)

    @classmethod
    def __start_search_game_request(cls, request):
        json_request = cls.__network_core(request)
        return json_request

    @classmethod
    def check_entry_account(cls, request):
        try:
            user = cls.__account_request(request)
            return True, user
        except Exception:
            return False, "login or password not in antry"

    @classmethod
    def registration(cls, request):
        try:
            return cls.__registration_account_request(request)
        except Exception:
            return "что то пошло не так"

    @classmethod
    def start_search_game(cls, request):
        try:
            return cls.__start_search_game_request(request)
        except Exception:
            return "что то пошло не так"
