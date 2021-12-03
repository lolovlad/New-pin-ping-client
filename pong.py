import pygame
import time
import os
import sys
from PySide6.QtWidgets import QApplication
from Models import LoginModel
from Controllers.LoginController import LoginController

from Core.GameSystem import GameSystem
from Core.MainMenu import MainMenu
from Model.DataBase import DataBase
from threading import Thread
from Core.Network import NetWork
from Model.DataBaseNetwork import DataBaseNetwork
from Class.CommandPars import CommandPars

counter = 0

user_name = 'Игрок'
ip = 42
color = 'white'


def network_core(net, mmr):
    net.send_message({"type_request": "start_search_game", "Name_user": user_name, "Color": color, "Ip_user": ip, "Mmr_user": mmr})
    while True:
        command = net.listener()
        if command is not None:
            DataBaseNetwork().add_list_command(command)
        else:
            break
    net.close()


def game_start(co=0):
    global user_name
    pygame.init()
    clock = pygame.time.Clock()
    GameSystem().game_init()
    pygame.display.set_caption(f'Ping-Pong 2.0 {user_name}')

    while DataBase().is_playing:
        clock.tick(120)
        GameSystem().update_game()
        pygame.display.update()
    pygame.quit()

    
def game_menu():
    global user_name, color
    app = QApplication(sys.argv)
    model = LoginModel()
    controller = LoginController(model)
    app.exec()


Thread(target=game_menu, args=(), daemon=True).start()
while True:
    if DataBase().last_button == "connect" and not DataBase().is_playing:
            user_name = "lol"
            color = ['white', 'red', 'green', 'blue', 'yellow'][0]
            DataBaseNetwork().attach(CommandPars())
            Thread(target=network_core, args=(NetWork(), 1000,), daemon=True).start()
            DataBase().last_button = "None"
    if DataBase().is_playing:
        game_start(counter)
    #os.execl(sys.executable, 'python', __file__, *sys.argv[1:])