from enum import Enum
from os import path, getcwd
from SupplementaryFiles.LoadGraph import load_graph_from_file
# from SupplementaryFiles.LoadGraphTxt import load_graph_from_file
from KivyFiles.KivyGraphTester import *
from GraphGeneration import HandmadeGraph
from SupplementaryFiles.Utils import Utils
from kivy.core.window import Window
from FitGraphs import FitGraphs

CONFIG_FILE_PATH = path.join("..", "game_config.txt")
GRAPH_CONFIG_PATH = path.join("..", "graph_config.txt")


# graph_file_path = "../GraphsData/Graph_1.xml"
graph_file_path = "../TestingGraphs/draft_graph_1.xml"


class GameType(Enum):
    VIEW_ONLY = 1
    ALLOW_PLAY = 2


def main(game_type, graph_data):
    if game_type == GameType.VIEW_ONLY:
        game = DisplayApp(graph_data)
    elif game_type == GameType.ALLOW_PLAY:
        button_presses = []
        # This needs to be more versatile
        test_screen = TestScreen(graph_data, button_presses, 0.2)
        test_screen.graph_config = "../GraphsData/graph_config.txt"
        game = GraphGameApp(test_screen)
    game.run()


if __name__ == "__main__":
    # Window.size = (1920, 1090)
    Window.size = (800, 600)
    HandmadeGraph.create_draft_graph_1()
    Utils.read_game_config_file(CONFIG_FILE_PATH)
    Utils.read_graph_config_file(GRAPH_CONFIG_PATH)
    Utils.image_folder = path.join("..", Utils.image_folder)
    # game_type = GameType.VIEW_ONLY
    game_type = GameType.ALLOW_PLAY

    graph = load_graph_from_file(graph_file_path)
    # graph = HandmadeGraph.create_tablet_graph_1()
    FitGraphs(graph)
    main(game_type, graph)
