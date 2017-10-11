import kivy
from enum import Enum

from Main import CONFIG_FILE_PATH

kivy.require('1.9.1')
from SupplementaryFiles.LoadGraph import load_graph_from_file
from KivyFiles.KivyGraphTester import *
from GraphGeneration import HandmadeGraph

graph_file_path = "../GraphsData/Graph_1.xml"
graph_data = HandmadeGraph.create_draft_graph_2()


class GameType(Enum):
    VIEW_ONLY = 1
    ALLOW_PLAY = 2


def main(game_type, graph_data):
    if game_type == GameType.VIEW_ONLY:
        game = DisplayApp(graph_data)
    elif game_type == GameType.ALLOW_PLAY:
        button_presses = []
        # This needs to be more versatile
        game = GraphGameApp(TestScreen(graph_data, button_presses, 0.2))
    game.run()


if __name__ == "__main__":
    Utils.read_config_file(CONFIG_FILE_PATH, True)
    game_type = GameType.ALLOW_PLAY
    if game_type == GameType.VIEW_ONLY:
        graph = load_graph_from_file(graph_file_path)
    else:
        graph = load_graph_from_file(graph_file_path)
        #graph = graph_data
    main(game_type, graph)
