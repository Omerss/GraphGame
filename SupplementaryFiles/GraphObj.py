import logging
import os
import uuid

from datetime import datetime
datetime.utcnow()
from SupplementaryFiles import Utils
from SupplementaryFiles.Enums import Colours, Shapes
from SupplementaryFiles.NodeObject import NodeObject


class GraphObject:
    node_list = []
    connections = []
    size = {"max_x": 1000, "max_y": 1000}
    line_colour = Colours.red
    node_count = 10
    max_neighbors = 5
    extra_distance = 25

    def __init__(self, config_file=None, max_x=None, max_y=None, node_count=None, max_neighbors=None, extra_distance=None):
        if config_file:
            assert(os.path.exists(config_file))
            self.config = Utils.read_config_file(config_file)
            self.size = {"max_x": self.config.getint('GeneralParams', 'GraphSizeX'),
                         "max_y": self.config.getint('GeneralParams', 'GraphSizeY')}
            self.node_count = self.config.getint("GeneralParams", "NodeCount")
            self.max_neighbors = self.config.getint('NodeData', 'MaxNeighbors')
            self.extra_distance = self.config.getint('NodeData', 'ExtraDistance')
        else:
            # Creating graph by parameters and not config
            self.size = {"max_x": max_x,
                         "max_y": max_y}
            self.node_count = node_count
            self.max_neighbors = max_neighbors
            self.extra_distance = extra_distance
        self.node_list = []
        self.connections = []

    def create_graph(self):
        for i in range(self.node_count):
            self.nodeList.append(NodeObject())

    def add_node(self, x_loc, y_loc, node_colour=Colours.red, node_shape=Shapes.circle, node_size=50, serial=None, real=True):
        """
        :param serial: A specific serial for the node.
        :param x_loc: The x location of the node
        :param y_loc: The y location of the node
        :param node_colour: Colour of the node
        :param node_shape: Shape of the node
        :param node_size: Size of the node (int value)
        :return: the new node of type NodeObject
        """
        if self.size["max_x"] < x_loc + node_size and 0 > x_loc - node_size:
            raise Exception("Error! Coordinate of node is out of bound: {}".format(x_loc))
        if self.size["max_y"] < y_loc + node_size and 0 > y_loc - node_size:
            raise Exception("Error! Coordinate of node is out of bound: {}".format(y_loc))

        location = {'x': x_loc, 'y': y_loc}
        if serial is not None:
            if self.get_node_by_serial(serial) is not None:
                print("Error - Trying to add a node with an existing serial")
                return None
        else:
            serial = get_serial()
        new_node = NodeObject(serial=serial, location=location, size=node_size, colour=node_colour, shape=node_shape, real=real)
        self.node_list.append(new_node)
        return new_node

    def get_possible_connections(self, node_serial, allow_overflow=False):
        """
        Returns all possible nodes that can be connected to this specific node.
        :param node_serial:
        :param allow_overflow: should nodes that have their maximum amount of connections be inserted to the list
        :return: A list of node.serial of possible connections
        """

        # print "Getting possible connections for node '{}'".format(node_serial)
        main_node = self.get_node_by_serial(node_serial)
        # print "Node '{}' has '{}' neighbors".format(main_node.serial_num, len(main_node.neighbors))
        if len(main_node.neighbors) < self.max_neighbors or allow_overflow:
            logging.debug("Working with Node '{}'.".format(node_serial))
            for node_to_connect in self.node_list:
                # Node is not the main one
                if node_to_connect != main_node and\
                   node_to_connect.serial_num not in main_node.possible_neighbors and\
                   node_to_connect.serial_num not in main_node.neighbors:
                    # print "Checking Node '{}'.".format(node_to_connect.serial_num)
                    if len(node_to_connect.neighbors) < self.max_neighbors or allow_overflow:
                        # Enumerate over all other nodes. check if any node is the the line of sight
                        # between node_to_connect and main_node
                        line_doesnt_cross = True
                        # print "Checking if other nodes possibly cross the view between the two nodes"
                        for check_node in self.node_list:
                            if check_node != node_to_connect and check_node != main_node:
                                if not self.is_node_far_enough(check_node, node_to_connect, main_node):
                                    line_doesnt_cross = False
                                    break
                        if line_doesnt_cross:
                            logging.debug("No obstacle between node {} and node {}. Adding node to list"\
                                .format(main_node.serial_num, node_to_connect.serial_num))
                            # Line between Main and node_to_connect does't cut any nodes
                            main_node.possible_neighbors.add(node_to_connect.serial_num)
                            node_to_connect.possible_neighbors.add(main_node.serial_num)
        logging.debug("Node '{}' has these possible neighbors: {}".format(main_node.serial_num, main_node.possible_neighbors))
        return main_node.possible_neighbors

    def get_best_connection(self, node, allow_overflow=False):
        """

        :param node: The node which we want to check the best connections for
        :param allow_overflow: If node can have more than max connections
        :return: returns the best possible connection from the list. A serial number
        """
        # Possibilities = shortest connection, nax number of connections
        # TODO - Make an actual check for best connection
        connection_count = 100
        best_node = ""
        # Getting node with minimal amount of connections
        for check_serial in node.possible_neighbors:
            check_node = self.get_node_by_serial(check_serial)
            if len(check_node.neighbors) < connection_count:
                best_node = check_node
                connection_count = len(best_node.neighbors)
        logging.debug("Choose node {0} with {1} connections".format(best_node.serial_num, connection_count))
        return best_node.serial_num

    def get_node_by_serial(self, serial):
        for node in self.node_list:
            if node.serial_num == serial:
                return node
        return None


    def is_node_far_enough(self, main_node, node_1, node_2):
        """
        Checks if the distance between main node and a possible line between node_1 and node_2 is too close.
        Meaning is main_node in the line of sight between line_1 and line_2. If so than line_1 cannot connect
        to line_2
        :param main_node: The node not connected to other nodes
        :param node_1:
        :param node_2:
        :return: True if the distance between main_node and the possible line between node_1 and node_2 is large enough
        """
        distance = main_node.distance_from_line(node_1, node_2)
        if distance >= main_node.size/2 + self.extra_distance:
            return True
        else:
            # print "Distance is too small. Node crossed the line of sight of the other nodes."
            # print "The distance between node '{}' and the line of sight between node '{}' and node {} is {}." \
            #     .format(main_node.serial_num, node_1.serial_num, node_2.serial_num, distance)
            return False

    def connect_nodes(self, node1, node2, allow_overflow=False):
        """
        Connects both nodes, remove each from the list of  possible neighbors of the other and adds to the list of
        neighbors.
        :param allow_overflow: If node can have more than max connections
        :return: True if nodes were connected,
        Raise exception if problem accrued
        """
        if (len(node1.neighbors) >= self.max_neighbors or
            len(node2.neighbors) >= self.max_neighbors)\
                and not allow_overflow:
                raise Exception("One of the nodes has too many neighbors")
        if node1.serial_num in node2.possible_neighbors and node2.serial_num in node1.possible_neighbors:
            # Connect nodes
            node1.neighbors.add(node2.serial_num)
            node2.neighbors.add(node1.serial_num)
            # Removes from future possible connections
            node1.possible_neighbors.remove(node2.serial_num)
            node2.possible_neighbors.remove(node1.serial_num)
            self.connections.append((min(node1.serial_num, node2.serial_num), max(node1.serial_num, node2.serial_num)))
            return True
        else:
            raise Exception("Connection between the two nodes is not possible")

    def get_connections(self):
        return self.connections


def get_serial():
    #return str(datetime.now().strftime("%M%S%f"))
    return str(uuid.uuid4())






