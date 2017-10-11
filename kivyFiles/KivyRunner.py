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


def main(game_type, graph):
    if game_type == GameType.VIEW_ONLY:
        game = load_graph_from_file(graph)
    elif game_type == GameType.ALLOW_PLAY:
        button_presses = []
        # This needs to be more versatile
        game = GraphGameApp(TestScreen(graph, button_presses, 0.2))
    game.run()


if __name__ == "__main__":
    main(GameType.VIEW_ONLY, graph_file_path)
