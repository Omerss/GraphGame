import kivy
from enum import Enum

kivy.require('1.9.1')
from SupplementaryFiles.LoadGraph import load_graph_from_file
from KivyGraphTester import *
from GraphGeneration import HandmadeGraph

graph_file_path = "../GraphsData/draft_graph2.xml"
graph_data = HandmadeGraph.create_draft_graph_2()


class GameType(Enum):
    VIEW_ONLY = 1
    ALLOW_PLAY = 2


def main(type, graph_data):
    if game_type == GameType.VIEW_ONLY:
        game = DisplayApp(graph)
    elif game_type == GameType.ALLOW_PLAY:
        button_presses = []
        # This needs to be more versatile
        game = GraphGameApp(TestScreen(graph, button_presses, 0.2))
    game.run()


if __name__ == "__main__":
    game_type = GameType.VIEW_ONLY
    
    if game_type == GameType.VIEW_ONLY:
        graph = load_graph_from_file(graph_file_path)
    else:
        graph = graph_data
    main(game_type, graph)
