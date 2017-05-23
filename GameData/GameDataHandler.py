

from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.LineEquation import LineEquation, LINES_ALWAYS_MEET

"""
Handles all data return from the window. Constructs a new graph based on the supplied data.
"""


class GameDataHandler:
    def __init__(self, config):
        # basic_config -
        self.edges = []
        self.nodes = []
        self.graph = GraphObject(config)
        self.extra_edges = []

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
            if edge[0].is_real():
                node_0 = self.graph.get_node_by_serial(edge[0].serial_num)
            else:
                node_0 = self.graph.add_node(edge[0].x, edge[0].y, node_size=1, real=False)

            if edge[1].is_real():
                node_1 = self.graph.get_node_by_serial(edge[1].serial_num)
            else:
                node_1 = self.graph.add_node(edge[1].x, edge[1].y, node_size=1, real=False)

            if node_1.serial_num not in node_0.possible_neighbors:
                node_0.possible_neighbors.add(node_1.serial_num)
            if node_0.serial_num not in node_1.possible_neighbors:
                node_1.possible_neighbors.add(node_0.serial_num)
            self.graph.connect_nodes(node_0, node_1, allow_overflow=True)


            # if not edge[0].is_real() and not edge[1].is_real():
            #     tmp_node_0 = self.graph.add_node(edge[0].x, edge[0].y, node_colour=node.colour, node_size=node.size,
            #                                      real=False)
            #     tmp_node_1 = self.graph.add_node(edge[1].x, edge[1].y, node_colour=node.colour, node_size=node.size,
            #                                      real=False)
            #     tmp_node_0.possible_neighbors.add(tmp_node_1.serial_num)
            #     tmp_node_1.possible_neighbors.add(tmp_node_0.serial_num)
            #     self.graph.connect_nodes(tmp_node_0, tmp_node_1, allow_overflow=True)
            #
            # if edge[0].is_real() and not edge[1].is_real():
            #     node = self.graph.get_node_by_serial(edge[0].serial_num)
            #     tmp_node = self.graph.add_node(edge[1].x, edge[1].y, node_colour=node.colour, node_size=node.size, real=False)
            #     node.possible_neighbors.add(tmp_node.serial_num)
            #     tmp_node.possible_neighbors.add(node.serial_num)
            #     self.graph.connect_nodes(node, tmp_node, allow_overflow=True)
            #
            # if not edge[0].is_real() and edge[1].is_real():
            #     node = self.graph.get_node_by_serial(edge[1].serial_num)
            #     tmp_node = self.graph.add_node(edge[0].x, edge[0].y, node_colour=node.colour, node_size=node.size, real=False)
            #     node.possible_neighbors.add(tmp_node.serial_num)
            #     tmp_node.possible_neighbors.add(node.serial_num)
            #     self.graph.connect_nodes(node, tmp_node, allow_overflow=True)
            #
            # if edge[1].is_real() and edge[0].is_real():
            #     node_0 = self.graph.get_node_by_serial(edge[0].serial_num)
            #     node_1 = self.graph.get_node_by_serial(edge[1].serial_num)
            #     node_0.possible_neighbors.add(node_1.serial_num)
            #     node_1.possible_neighbors.add(node_0.serial_num)
            #     self.graph.connect_nodes(node_0, node_1, allow_overflow=True)

            if edge not in self.extra_edges:
                self.extra_edges.append(edge)
        self.trim_data()

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
                    #print ("Lines meet and intersect with each other - They are the same line")
                    return True
                else:
                    #print ("Line have the same parameters but we are not sure of they meet")
                    return False

    def connect_edges(self, edge_1, edge_2):
        """
        The longest distance in an edge is the distance between the real nodes of that edge.
        We clean all existing connections and then connect the two nodes that are furthest from each other.
        :param edge_1, edge_2: An edge defined by a tuple of NodeObjects
        """
        # Cleaning all existing connection
        if edge_1 in self.extra_edges:
            self.extra_edges.remove(edge_1)
        if edge_2 in self.extra_edges:
            self.extra_edges.remove(edge_2)

        self.clean_connection(edge_1[0], edge_1[1])
        self.clean_connection(edge_1[1], edge_1[0])
        self.clean_connection(edge_2[0], edge_2[1])
        self.clean_connection(edge_2[1], edge_2[0])

        node_1_serial, node_2_serial = self.get_furthest_nodes(edge_1[0], edge_1[1], edge_2[0], edge_2[1])
        node_1 = self.graph.get_node_by_serial(node_1_serial)
        node_2 = self.graph.get_node_by_serial(node_2_serial)

        # connect the right nodes
        self.connect_nodes(node_1, node_2)
        if node_1.x < node_2.x:
            self.extra_edges.append((node_1, node_2))
        else:
            self.extra_edges.append((node_2, node_1))

    def clean_connection(self, main_node, node_to_remove):
        """
        Removed all connection from main_node regarding node_to_remove
        :param node_to_remove: The node to remove
        :param main_node: The node we want to remove data from 
        :return: 
        """
        node = self.graph.get_node_by_serial(main_node.serial_num)
        if node_to_remove.serial_num in node.neighbors:
            node.neighbors.remove(node_to_remove.serial_num)
        if node_to_remove.serial_num in node.possible_neighbors:
            node.possible_neighbors.remove(node_to_remove.serial_num)

    def connect_nodes(self, first_node, second_node):
        """
        Connect the two nodes in the graph.
        Also add the new edge to the extra_edges list
        """
        node_0 = self.graph.get_node_by_serial(first_node.serial_num)
        node_1 = self.graph.get_node_by_serial(second_node.serial_num)

        node_0.possible_neighbors.add(node_1.serial_num)
        node_1.possible_neighbors.add(node_0.serial_num)
        self.graph.connect_nodes(node_0, node_1, allow_overflow=True)
        if node_0.x < node_1.x:
            edge = (node_0, node_1)
        else:
            edge = (node_1, node_0)
        self.extra_edges.append(edge)

    @staticmethod
    def get_furthest_nodes(*args):
        """
        :param args: a list of NodeObjects
        :return: The serial numbers of the two furthest nodes from each of other.
        """
        from SupplementaryFiles.NodeObject import NodeObject
        node_list = {}
        for node in args:
            if type(node) != NodeObject:
                raise Exception("One of the arguments is not of type NodeObjects")
            distance_list = []
            for other_node in args:
                if other_node != node:
                    distance_list.append((other_node,node.distance(other_node)))
            node_list[node.serial_num] = distance_list

        best_distance = 0
        best_pair = ()
        for node in args:
            for other_node in node_list[node.serial_num]:
                if other_node[1] > best_distance:
                    best_pair = (node.serial_num, other_node[0].serial_num)
                    best_distance = other_node[1]
        return best_pair


