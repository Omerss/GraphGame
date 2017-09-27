import os
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame
from KivyGraphTester import *

if __name__ == "__main__":
    button_presses = []
    #GraphTabletGame require a signal parameter - thats why the main.py doesn't work
    game = GraphTabletGame(create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd())), None,
     button_width=100, dim={"max_x": 800, "max_y": 600})

    # game = GraphTabletGame(MyGameLayout.get_graph_obj1(), None, button_width=100, dim={"max_x": 800, "max_y": 600})
    # game  = GraphGameApp(button_presses)
    game.run()
    print game.button_presses