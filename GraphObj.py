from random import random

import Utils
from NodeObject import NodeObject


class GraphObject():
    node_list = []
    size = {}
    extra_distance = 1
    max_neighbors = 4

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
        location = {'x': x_loc, 'y': y_loc}
        serial = self.get_serial(location)
        new_node = NodeObject(serial=serial, location=location, size=node_size, colour=node_colour, shape=node_shape)
        self.node_list.append(new_node)
        return new_node

    def get_possible_connections(self, node_serial, allow_overflow=False):
        """
        Returns all possible nodes that can be connected to this specific node.
        :param node_serial:
        :param allow_overflow: should nodes that have their maximum amount of connections be inserted to the list
        :return: A list of node.serial of possible connections
        """
        node_list = ()
        main_node = self.get_node_by_serial(node_serial)
        for node_to_connect in self.node_list:
            # Node is not the main one
            if len(node_to_connect.neighbors) < self.max_neighbors or allow_overflow:
                if node_to_connect != main_node:
                    # Enumerate over all other nodes
                    line_doesnt_cross = True
                    for check_node in self.node_list:
                        if check_node != node_to_connect and check_node != main_node:
                            if not self.is_node_far_enough(check_node, node_to_connect, main_node):
                                line_doesnt_cross = False
                    if line_doesnt_cross:
                        # Line between Main and node_to_connect does't cut any nodes
                        node_list.__add__(node_to_connect.serial)

        main_node.possible_connections = node_list
        return node_list

    def get_best_connection(self, node, allow_overflow=False):
        """

        :param node_list: a list of possible connections
        :return: returns the best possible connection from the list. A serial number
        """
        # Possibilities = shortest connection, nax number of connections
        node_id = node.possible_connections.pop()
        node.possible_connections.add(node_id)
        return node_id

    def get_node_by_serial(self, serial):
        result = None
        for node in self.node_list:
            if node.serial_num == serial:
                result = node
        return result

    def is_node_far_enough(self, main_node, node_1, node_2):
        """
        :param main_node:
        :param p1:
        :param p2:
        :return:
        """
        distance = main_node.distance_from_line(node_1, node_2)
        if distance >= main_node.size + self.extra_distance:
            return True
        else:
            return False

    def get_serial(self, location):
        return hash(location)

