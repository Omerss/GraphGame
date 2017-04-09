import random
import time

from GraphObj import GraphObject
from NodeObject import NodeObject
from kivyFiles.GraphTabletGame import GraphTabletGame
from LineEquation import LineEquation, LINES_ALWAYS_MEET

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
        number_of_real_nodes = 20
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
            if edge[0].real is False and edge[1].real is False:
                if edge not in self.extra_edges: self.extra_edges.append(edge)
            if edge[0].real is True and edge[1].real is False:
                node = self.graph.get_node_by_serial(edge[0].serial_num)
                tmp_node = self.graph.add_node(edge[1].x, edge[1].y, node_colour=node.colour, node_size=node.size, real=False)

                node.possible_neighbors.add(tmp_node.serial_num)
                tmp_node.possible_neighbors.add(node.serial_num)
                self.graph.connect_nodes(node, tmp_node, allow_overflow=True)
                if edge not in self.extra_edges: self.extra_edges.append(edge)
            if edge[0].real is False and edge[0].real is True:
                node = self.graph.get_node_by_serial(edge[1].serial_num)
                tmp_node = self.graph.add_node(edge[0].x, edge[0].y, node_colour=node.colour, node_size=node.size, real=False)

                node.possible_neighbors.add(tmp_node.serial_num)
                tmp_node.possible_neighbors.add(node.serial_num)
                self.graph.connect_nodes(node, tmp_node, allow_overflow=True)
                if edge not in self.extra_edges: self.extra_edges.append(edge)
            if edge[1].real is True and edge[0].real is True:
                node_0 = self.graph.get_node_by_serial(edge[0].serial_num)
                node_1 = self.graph.get_node_by_serial(edge[1].serial_num)

                node_0.possible_neighbors.add(node_1.serial_num)
                node_1.possible_neighbors.add(node_0.serial_num)
                self.graph.connect_nodes(node_0, node_1, allow_overflow=True)
                if edge not in self.extra_edges: self.extra_edges.append(edge)

    def trim_data(self):
        """
        Goes over all of the data that is saved and trims nodes and edges.
        Connects fake nodes to real ones if we found the actual node
        connects open edges together if possible
        """
        for edge in self.extra_edges:
            slope = abs(edge[0].slope(edge[1]))
            for other_edge in self.extra_edges:
                if other_edge != edge:
                    if slope == other_edge[0].slope(other_edge[1]):
                        if self.two_edges_are_one(edge, other_edge):
                            self.connect_edges(edge, other_edge)

    @staticmethod
    def two_edges_are_one(edge_1, edge_2):
        """
        Checks if the two edges are actually a single edge.
        :return: True if edges are 100% the same one
        """
        if edge_1[0].slope(edge_1[1]) != edge_2[0].slope(edge_2[1]):
            print("Error - slopes of both edges are not the same")
            return False
        else:
            eq1 = LineEquation.create_equation(edge_1[0], edge_1[1])
            eq2 = LineEquation.create_equation(edge_2[0], edge_2[1])
            # Check collision point
            collision_point = LineEquation.get_equation_collision_point(eq1, eq2)
            if collision_point == LINES_ALWAYS_MEET:
                # Lines have the same slope + const. Big change they are the same one.
                if LineEquation.check_collision_point(eq1, eq2):
                    print ("Lines meet and intersect with each other - They are the same line")
                    return True
                else:
                    print ("Line have the same parameters but we are not sure of they meet")
                    return False

    def connect_edges(self, edge_1, edge_2):
        """
        We know the edges are the same one. Connecting them
        Case 1 - One edge is connected to two real nodes. Other edge only connects to the left node and the other part to a fake node
        Case 2 - One edge is connected to two real nodes. Other edge only connects to the right node and the other part to a fake node (Mirror case 1)
        Case 3 - Both edge each connect to one real node and one fake node. Both real nodes are different
        Case 4 - Both edges connect to a real node - Real node is on the left.  Both edge's other node is a fake one
        Case 5 - Both edges connect to a real node - Real node is on the right.  Both edge's other node is a fake one (Mirror case 4)
        case 6 - One edge is connected to a real node and to a fake node - Real node is on the left. Other edge connects to two fake nodes.
        case 7 - One edge is connected to a real node and to a fake node - Real node is on the right. Other edge connects to two fake nodes. (Mirror case 6)
        case 8 - Both edge have two fake nodes
        :return: None
        """
        left_edge = edge_1 if edge_1[0].x <= edge_2[0].x else edge_2
        right_edge = edge_1 if edge_1[0].x > edge_2[0].x else edge_2
        if left_edge[0].is_real():
            # case 1,2,3,4,7
            if right_edge[1].is_real():
                # case 1,2,3
                pass
            else:
                # case 4,7
                pass
        else:
            # case 5,6,8
            if right_edge[1].is_real():
                # case 5, 6
                if left_edge[1].x == right_edge[1].x:
                    # case 5
                    node = self.graph.get_node_by_serial(left_edge[1].serial_num)
                    if right_edge[0].serial_num not in node.neighbors:
                        Exception("Could not find fake node in list")
                    node.neighbors.remove(right_edge[0].serial_num)
                    node.possible_neighbors.remove(right_edge[0].serial_num)
                    self.extra_edges.remove(right_edge)
                else:
                    # case 6
                    pass

            else:
                # case 8
                if left_edge[1].x > right_edge[1].x:
                    # left edge overlaps right edge. We can dump edge 2
                    self.extra_edges.remove(right_edge)
                else:
                    # We create a new edge tuple combining both edges
                    new_edge = (left_edge[0], right_edge[1])
                    self.extra_edges.remove(left_edge)
                    self.extra_edges.remove(right_edge)
                    self.extra_edges.append(new_edge)


        self.extra_edges


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

