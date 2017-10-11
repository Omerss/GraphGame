import os
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame
from KivyGraphTester import *
from random import randint
from GraphGeneration import HandmadeGraph
from SupplementaryFiles.LoadGraph import load_graph_from_file


import os
import kivy
from enum import Enum

kivy.require('1.9.1')

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame
from KivyGraphTester import *
from random import randint
from GraphGeneration import HandmadeGraph

graph_file_path = "../GraphsData/draft_graph2.xml"


class GameType(Enum):
    VIEW_ONLY = 1
    ALLOW_PLAY = 2


def main(game_type):
    if game_type == GameType.VIEW_ONLY:
        game = load_graph_from_file(graph_file_path)
    elif game_type == GameType.ALLOW_PLAY:
        button_presses = []
        game = GraphGameApp(TestScreen(HandmadeGraph.create_draft_graph_2(), button_presses, 0.2))
    game.run()

