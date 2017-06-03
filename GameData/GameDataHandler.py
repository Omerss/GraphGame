import sys
from structlog import get_logger
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.LineEquation import LineEquation, LINES_ALWAYS_MEET

"""
Handles all data return from the window. Constructs a new graph based on the supplied data.
"""


class GameDataHandler:
    def __init__(self, config):
        # basic_config -
        self.edges = []
        self.graph = GraphObject(config)
        self.extra_edges = []
        self.new_edges = []
        self.edges_to_add = []
        self.log = get_logger()

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
            if node.is_real() and self.graph.get_node_by_serial(node.serial_num) is None:
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

            if edge not in self.extra_edges:
                self.extra_edges.append(edge)

        self.log.info("Timing data from graph")
        self.trim_data()
        self.log.info("Adding extra edges to edge list", edges_to_add=self.edges_to_add)
        if len(self.edges_to_add) > 0:
            self.extra_edges += self.edges_to_add
        self.clean_duplicate_nodes()

    def trim_data(self):
        """
        Goes over all of the data that is saved and trims nodes and edges.
        Connects fake nodes to real ones if we found the actual node
        connects open edges together if possible
        """
        slope_set = set()
        for edge in self.extra_edges:
            slope_set.add(edge[2])
        sorted(slope_set)
        for slope in slope_set:
            edges_to_check = []
            for edge in self.extra_edges:
                if edge[2] == slope:
                    edges_to_check.append(edge)
            if len(edges_to_check) > 1:
                # we have two edges with the same slope!
                # Removing all edges from list. We add only the relevant ones later on
                for item in edges_to_check:
                    self.extra_edges.remove(item)

                for edge in edges_to_check:
                    edges_to_check.remove(item)
                    did_edge_have_match = False
                    for other_edge in edges_to_check:
                        if self.two_edges_are_one(edge, other_edge):
                            self.connect_edges(edge, other_edge)
                            did_edge_have_match = True
                    if not did_edge_have_match:
                        self.edges_to_add.append(edge)

    @staticmethod
    def two_edges_are_one(edge_1, edge_2):
        """
        Checks if the two edges are actually a single edge.
        :return: True if edges are 100% the same one
        """
        log = get_logger()
        log.info("Checking if two edges are one", edge_1=edge_1, edge_2=edge_2)
        if edge_1[0].slope(edge_1[1]) != edge_2[0].slope(edge_2[1]):
            log.debug("Slopes of both edges are not the same")
            return False
        else:
            eq1 = LineEquation.create_equation(edge_1[0], edge_1[1])
            eq2 = LineEquation.create_equation(edge_2[0], edge_2[1])
            # Check collision point
            collision_point = LineEquation.get_equation_collision_point(eq1, eq2)
            log.debug("Found collision point of both edges", point=collision_point, eq1=eq1, eq2=eq2)
            if collision_point == LINES_ALWAYS_MEET:
                # Lines have the same slope + const. Big change they are the same one.
                if LineEquation.check_collision_point(eq1, eq2):
                    log.debug("Lines meet and intersect with each other - They are the same line")
                    return True
                else:
                    log.debug("Lines have the same parameters but we are not sure of they meet")
                    return False

    def connect_edges(self, edge_1, edge_2):
        """
        The longest distance in an edge is the distance between the real nodes of that edge.
        We clean all existing connections and then connect the two nodes that are furthest from each other.
        :param edge_1, edge_2: An edge defined by a tuple of NodeObjects
        """
        # Cleaning all existing connection
        self.log.debug("Connecting edges", edge1=edge_1, edge2=edge_2)
        if edge_1 in self.extra_edges:
            self.log.debug("Removing edge from extra edges", removed_edge=edge_1)
            self.extra_edges.remove(edge_1)
        if edge_2 in self.extra_edges:
            self.log.debug("Removing edge from extra edges", removed_edge=edge_2)
            self.extra_edges.remove(edge_2)

        if edge_1[0] is None or edge_1[1] is None or edge_2[0] is None or edge_2[1] is None:
            raise Exception("Cleaning Nodes failed - At least one of the nodes does not exist")

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
            self.edges_to_add.append((node_1, node_2, edge_1[2]))
        else:
            self.edges_to_add.append((node_2, node_1, edge_1[2]))

    def clean_connection(self, main_node, node_to_remove):
        """
        Removed all connection from main_node regarding node_to_remove
        :param node_to_remove: The node to remove
        :param main_node: The node we want to remove data from 
        :return: 
        """
        self.log.info("Cleaning connection to another node", main_node=main_node.serial_num,
                      node_to_remove=node_to_remove.serial_num)
        node = self.graph.get_node_by_serial(main_node.serial_num)
        if node is None:
            raise Exception("Node '{}' was not found in node list. Node list = {}".format(main_node, self.graph.node_list))
        if node_to_remove.serial_num in node.neighbors:
            node.neighbors.remove(node_to_remove.serial_num)
        if node_to_remove.serial_num in node.possible_neighbors:
            node.possible_neighbors.remove(node_to_remove.serial_num)

    def connect_nodes(self, first_node, second_node):
        """
        Connect the two nodes in the graph.
        """
        node_0 = self.graph.get_node_by_serial(first_node.serial_num)
        node_1 = self.graph.get_node_by_serial(second_node.serial_num)

        node_0.possible_neighbors.add(node_1.serial_num)
        node_1.possible_neighbors.add(node_0.serial_num)
        self.graph.connect_nodes(node_0, node_1, allow_overflow=True)

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

    def clean_duplicate_nodes(self):
        pass



