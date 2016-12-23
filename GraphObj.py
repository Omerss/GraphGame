import Utils
from NodeObject import NodeObject
from Enums import Colours, Shapes


class GraphObject:
    node_list = []
    connections = []
    size = {"max_x": 1000, "max_y": 1000}
    line_colour = Colours.white
    node_count = 10
    max_neighbors = 5
    extra_distance = 25

    def __init__(self, config_file=None, **kwargs):
        if config_file:
            self.config = Utils.read_config_file(config_file)
            self.size = {"max_x": self.config.getint('GeneralParams', 'GraphSizeX'),
                         "max_y": self.config.getint('GeneralParams', 'GraphSizeY')}
            self.node_count = self.config.getint("GeneralParams", "NodeCount")
            self.max_neighbors = self.config.getint('NodeData', 'MaxNeighbors')
            self.extra_distance = self.config.getint('NodeData', 'ExtraDistance')
        else:
            # Creating graph by parameters and not config
            self.size = {"max_x": kwargs["max_x"],
                         "max_y": kwargs["max_y"]}
            self.node_count = kwargs["node_count"]
            self.max_neighbors = kwargs["max_neighbors"]
            self.extra_distance = kwargs["extra_distance"]
        self.node_list = []
        self.connections = []

    def create_graph(self):
        for i in range(self.node_count):
            self.nodeList.append(NodeObject())

    def add_node(self, x_loc, y_loc, node_colour=Colours.black, node_shape=Shapes.circle, node_size=50):
        """
        :param x_loc: The x location of the node
        :param y_loc: The y location of the node
        :param node_colour: Colour of the node
        :param node_shape: Shape of the node
        :param node_size: Size of the node (int value)
        :return: the new node of type NodeObject
        """
        assert self.size["max_x"] >= x_loc + node_size and 0 <= x_loc - node_size, \
            "Error! Coordinate of node is out of bound: {}".format(x_loc)
        assert self.size["max_y"] >= y_loc + node_size and 0 <= y_loc - node_size, \
            "Error! Coordinate of node is out of bound: {}".format(y_loc)

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

        # print "Getting possible connections for node '{}'".format(node_serial)
        main_node = self.get_node_by_serial(node_serial)
        # print "Node '{}' has '{}' neighbors".format(main_node.serial_num, len(main_node.neighbors))
        if len(main_node.neighbors) < self.max_neighbors or allow_overflow:
            for node_to_connect in self.node_list:
                # Node is not the main one
                if node_to_connect != main_node and\
                   node_to_connect.serial_num not in main_node.possible_neighbors and\
                   node_to_connect.serial_num not in main_node.neighbors:
                    print "working with Node '{}' has {} neighbors".format(node_to_connect.serial_num,
                                                                                  len(node_to_connect.neighbors))
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
                            print "No obstacle between node {} and node {}. Adding node to list"\
                                .format(main_node.serial_num, node_to_connect.serial_num)
                            # Line between Main and node_to_connect does't cut any nodes
                            main_node.possible_neighbors.add(node_to_connect.serial_num)
                            node_to_connect.possible_neighbors.add(main_node.serial_num)
        print "Node '{}' has these possible neighbors: {}".format(main_node.serial_num, main_node.possible_neighbors)
        return main_node.possible_neighbors

    def get_best_connection(self, node, allow_overflow=False):
        """

        :param node: The node which we want to check the best connections for
        :param allow_overflow: If node can have more than max connections
        :return: returns the best possible connection from the list. A serial number
        """
        # Possibilities = shortest connection, nax number of connections
        # TODO - Make an actual check for best connection
        node_id = node.possible_neighbors.pop()

        node.possible_neighbors.add(node_id)
        return node_id

    def get_node_by_serial(self, serial):
        result = None
        for node in self.node_list:
            if node.serial_num == serial:
                return node
        raise Exception("Node '{}' was not found in node list. Node list = {}".format(serial, self.node_list))

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
        print "The distance between node '{}' and the line of sight between node '{}' and node {} is {}."\
            .format(main_node.serial_num, node_1.serial_num, node_2.serial_num, distance)
        if distance >= main_node.size/2 + self.extra_distance:
            return True
        else:
            # print "Distance is too small. Node crossed the line of sight of the other nodes."
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

    @staticmethod
    def get_serial(location):
        return hash(frozenset(location.items()))
