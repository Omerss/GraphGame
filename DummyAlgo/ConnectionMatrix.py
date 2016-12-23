import math
import numpy as np

from NodeObject import NodeObject
from Enums import Colours, Shapes

MIN_VALUE = 0.0001
MAX_VALUE = 1


class ConnectionMatrix:
    """
    ConnectionMatrix hold all possible connection between all nodes.
    """
    # probability_matrix is a dictionary object containing a dictionary for each other node
    probability_matrix = {}
    node_list = []

    def __init__(self, num_of_nodes):
        self.node_list = []
        for i in range(num_of_nodes):
            self.node_list.append(NodeObject(i, {'x': None, 'y': None}, size=None))

    def update_connection_probability(self, node_1, node_2, new_probability):
        """
        Updates the relationship between two nodes.
        :param node_1\ node_2: The two nodes that have their relationship updated
        :param new_probability: a number between 0 and 1
        """
        assert (MAX_VALUE >= new_probability >= MIN_VALUE, "Error! new probability has impossible value: {}"
                .format(new_probability))
        self.add_node_to_matrix(node_1)
        self.add_node_to_matrix(node_2)
        self.probability_matrix[node_1][node_2] = new_probability
        self.probability_matrix[node_2][node_1] = new_probability

    def add_node_to_matrix(self, node_serial):
        """
        Added node with name 'node_serial' to the probability_matrix. If node already exist does nothing
        :param node_serial: The serial of the node
        :return: All node objects connected to that node
        """
        if node_serial not in self.probability_matrix.keys():
            self.probability_matrix[node_serial] = {}
        return self.probability_matrix[node_serial]


