import os
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame
from KivyGraphTester import *
from random import randint


if __name__ == "__main__":

    # button_presses = [randint(1, 4) for i in range (5)]
    kivy.core.window.Window.size = (800, 600)
    # game = GraphTabletGame(create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd())), None, None)
    # game = GraphTabletGame(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25))
    # game = GraphGameApp(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25))
    # game = GraphTabletGame(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25, False))
    #
    # for button in button_presses:
    #     game.press_button(button)
    #
    # game.run()
    # print button_presses

    game = DisplayApp(create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd())))
    game.run()
