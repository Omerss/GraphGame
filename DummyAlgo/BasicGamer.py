from KivyGraph import KivyGraph
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
        self.graph_game = get_tablet_game()

    def get_number_of_known_nodes(self):
        return len(self.known_graph.node_list)

    def add_view_to_db(self, view):
        for temp_node in view:
            pass

    def read_data_from_window(self):
        node_list = []
        return

    def do_move(self):
        graph_window = self.read_data_from_window()
        self.add_view_to_db(graph_window)


gamer = BasicGamer()

turn = 0
while turn < 10:
    gamer.do_move()