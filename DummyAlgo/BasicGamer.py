import random
import time

from GraphObj import GraphObject
from NodeObject import NodeObject
from kivyFiles.GraphTabletGame import GraphTabletGame
from ConnectionMatrix import ConnectionMatrix
from ProbabilityGraph import ProbabilityGraph

"""
The basic AI that plays the game
"""

edges = []
nodes = []


def read_data_from_window(tablet_game):
    """
    Gets data from the kivy game. Data = {'nodes': [NodeObject list]. 'edges':[(NodeObject, NodeObject)]}
    In edges, if NodeObject has serial = None
    :return:
    """
    node_list = []
    return node_list


class BasicGamer:
    def __init__(self, config):
        number_of_nodes = 100
        self.graph = GraphObject(config)
        self.extra_edges = []
        # self.connection_matrix = ConnectionMatrix(number_of_nodes)
        # self.known_graph = ProbabilityGraph(number_of_nodes)
        self.tablet_game = GraphTabletGame()
        self.tablet_game.build()

    def get_number_of_known_nodes(self):
        return len(self.known_graph.node_list)

    def add_view_to_db(self, view):
        """
        Go over the new view gotten from the game. For each new node add it to self.graph.node_list
        For each edge check both ends. if the node has real=False we know it's only a placeholder.
        Update the graph of BasicGamer
        :param view: A dictionary containing the data gotten from the screen
        :return: None
        """
        # Innumerate over the nodes
        for node in view['nodes']:
            if node.real is True and self.graph.get_node_by_serial(node.serial_num) is None:
                self.graph.add_node(node.x, node.y, node_colour=node.colour, node_size=node.size, serial=node.serial_num)

        # Innumerate over the edges
        for edge in view['edges']:
            if edge[0].real is False and edge[1].read is False:
                if edge not in self.extra_edges:
                    # Edge is an empty edge. copy it to the side for now
                    self.extra_edges.append(edge)
            if edge[0].real is True and edge[1].real is False:
                node = self.graph.get_node_by_serial(edge[0].serial_num)
                tmp_node = self.graph.add_node(edge[1].x, edge[1].y, node_colour=node.colour, node_size=node.size, real=False)
                self.graph.connect_nodes(node, tmp_node)
            if edge[1].real is True and edge[0].real is False:
                node = self.graph.get_node_by_serial(edge[1].serial_num)
                tmp_node = self.graph.add_node(edge[0].x, edge[0].y, node_colour=node.colour, node_size=node.size, real=False)
                self.graph.connect_nodes(node, tmp_node)
            if edge[1].real is True and edge[0].real is True:
                node_0 = self.graph.get_node_by_serial(edge[0].serial_num)
                node_1 = self.graph.get_node_by_serial(edge[1].serial_num)
                self.graph.connect_nodes(node_0, node_1)

    def do_move(self):
        btn_num = self.get_best_button()
        self.tablet_game.press_button(btn_num)
        print("Pressing button {0}".format(btn_num))
        graph_window = read_data_from_window(self.tablet_game)
        self.add_view_to_db(graph_window)
        print(self.graph)

    def get_best_button(self):
        # use A* search algorithm
        return random.randint(1, 4)

