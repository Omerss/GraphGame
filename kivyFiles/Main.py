import os
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame
from KivyGraphTester import *


if __name__ == "__main__":

    button_presses = []
    #kivy.core.window.Window.size = (400, 200)
    # game = GraphTabletGame(create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd())), None, None)
    # game = GraphTabletGame(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25))
    game  = GraphGameApp(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25))
    game.run()
    print game.button_presses