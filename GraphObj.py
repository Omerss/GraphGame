from random import random

#import Utils
from NodeObject import NodeObject
from Enums import Colours, Shapes


class GraphObject:
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

        for i in range(self.config["GeneralParams"]["NodeCount"]):
            self.nodeList.append(NodeObject())


    def add_node(self, x_loc, y_loc, node_colour=Colours.black, node_shape=Shapes.circle, node_size=1):
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
        Checks is the distance between main node and the line between node_1 and node_2
        :param main_node: The node not connected to other nodes
        :param node_1:
        :param node_2:
        :return: True if the distance between main_node and the possible line between node_1 and node_2 is large enough
        """
        distance = main_node.distance_from_line(node_1, node_2)
        if distance >= main_node.size + self.extra_distance:
            return True
        else:
            return False

    def connect_nodes(self, node1_serial, node2_serial, allow_overflow=False):
        """
        Connects both nodes, remove each from the list of  possible neighbors of the other and adds to the list of
        neighbors.
        :param allow_overflow: If node can have more than max connections
        :return: True if nodes were connected,
        Raise exception if problem accrued
        """
        node1 = self.get_node_by_serial(node1_serial)
        node2 = self.get_node_by_serial(node2_serial)
        if (len(node1.neighbors) >= self.max_neighbors or len(node2.neighbors) >= self.max_neighbors)\
                and not allow_overflow:
            raise Exception("One of the nodes has too many neighbors")
        if node1_serial in node2.possible_neighbors and node2_serial in node1.possible_connections:
            # Connect nodes
            node1.neighbors.__add__(node2_serial)
            node2.neighbors.__add__(node1.serial)

            # Removes from future possible connections
            node1.possible_neighbors.remove(node2.serial)
            node2.possible_neighbors.remove(node1.serial)
            return True
        else:
            raise Exception("Connection between the two nodes is not possible")


    def get_serial(self, location):
        return hash(location)

