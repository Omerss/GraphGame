import random
import time

from kivyFiles.GraphTabletGame import GraphTabletGame
from ConnectionMatrix import ConnectionMatrix
from ProbabilityGraph import ProbabilityGraph

"""
The basic AI that plays the game
"""


class BasicGamer:
    def __init__(self):
        number_of_nodes = 20
        self.connection_matrix = ConnectionMatrix(number_of_nodes)
        self.known_graph = ProbabilityGraph(number_of_nodes)
        self.tablet_game = GraphTabletGame()
        self.tablet_game.build()

    def get_number_of_known_nodes(self):
        return len(self.known_graph.node_list)

    def add_view_to_db(self, view):
        for temp_node in view:
            pass

    def read_data_from_window(self):
        node_list = []
        return node_list

    def do_move(self):
        btn_num = self.get_best_button()
        self.tablet_game.press_button(btn_num)
        print("Pressing button {0}".format(btn_num))
        graph_window = self.read_data_from_window()
        self.add_view_to_db(graph_window)

    def get_best_button(self):
        return random.randint(1, 4)

gamer = BasicGamer()

for turn in range(10):
    gamer.do_move()
    time.sleep(1)
