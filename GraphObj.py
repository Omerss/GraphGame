from random import random

import Utils
from NodeObject import NodeObject


class GraphObject():
    node_list = []
    size = {}

    def __init__(self, size):
        self.config = Utils.config
        for i in range (self.config['GeneralParams']['NodeCount']):
            self.node_list[i] = i
        size = size

    def create_graph(self):

        random.seed()
        location = (random.randint(0,self.size["x"]),random.randint(0,self.size["y"]))
        location2 = (random.randint(0, self.size["x"]), random.randint(0, self.size["y"]))
        node = NodeObject(location,1)
        node2 = NodeObject(location2, 1)

        for i in range(self.config["GeneralParams"]["NodeCount"]):
            self.nodeList.append(NodeObject())

    def add_node(self, x_loc, y_loc, node_colour=NodeObject.Colours.Black, node_shape=NodeObject.Shape.Circle,
                 node_size=1):
        """

        :param x_loc: The x location of the node
        :param y_loc: The y location of the node
        :param node_colour: Colour of the node
        :param node_shape: Shape of the node
        :param node_size: Size of the node (int value)
        :return: the new node
        """
        serial = 1
        location = {'x': x_loc, 'y': y_loc}
        new_node = NodeObject(serial=serial, location=location, size=node_size, colour=node_colour, shape=node_shape)
        self.node_list.append(new_node)
        return new_node

    def get_possible_connections(self):
        """
        Returns all possible nodes that can be connected to this specific node.
        :return: A list of node.serial of possible connections
        """
        return []

    def get_best_connection(self, node_list):
        """

        :param node_list: a list of possible connections
        :return: returns the best possible connection from the list
        """
        node_id = node_list[0]
        return node_id



