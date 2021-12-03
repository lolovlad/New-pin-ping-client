from Views import MainWindowView
from Model.DataBase import DataBase
from ClassLt.Models_json.ServerGame import ServerGame
from ClassLt.ServerRespons import ServerResponse
from ClassLt.Session import Session
from socket import gethostbyname, gethostname
from pykson import Pykson
from random import randint


class MainWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = MainWindowView(self, self.__model)
        self.__view.show()

    def start_search_game(self):
        address = gethostbyname(gethostname())
        #request = {"id_user": Session().session.id, "color": "white", "ip": address,
        #           "port": randint(5000, 9000), "type_request": "start_search_game"}
        #response = ServerResponse.start_search_game(request)
        #server_game = Pykson().from_json(response["response"]["server_game"], ServerGame)
        #if response["type_request"] == "add_list":
        self.__view.ui.start_game_button.setText("searching...")
        DataBase().last_button = "connect"
            #print(server_game.ip, server_game.port)


