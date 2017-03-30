import kivy
kivy.require('1.9.1')

from kivy.uix.widget import Widget
from random import randint


class KivyGraph(Widget):
    center_coor = (0,0)
    nodes = None
    edges = None
    center_node = None
    real_size = {'max_x': 800, 'max_y': 600}

    def __init__(self, center, size, **kwargs):
        super(KivyGraph, self).__init__(**kwargs)
        self.center_coor = center
        self.nodes = []
        self.edges = []
        self.real_size = size

    def add_node(self,node):
        """
        function adds a given node to graph's nodes list
        """
        self.nodes.append(node)

    def add_edge(self,edge):
        """
        function adds a given edge to graph's list of edges
        """
        self.edges.append(edge)

    def get_by_serial(self, serial):
        """
        :param serial:
        :return: a node from graph's nodes list associated with given serial
        """
        for node in self.nodes:
            if node.serial == serial:
                return node
        raise Exception("Node '{}' was not found in node list. Node list = {}".format(serial, self.nodes))

    def move_up(self, amount = 40):
        for node in self.nodes:
            node.move_y(amount)
        for edge in self.edges:
            edge.reset_edge()

    def move_down(self, amount = -40):
        for node in self.nodes:
            node.move_y(amount)
        for edge in self.edges:
            edge.reset_edge()

    def move_left(self, amount = -40):
        for node in self.nodes:
            node.move_x(amount)
        for edge in self.edges:
           edge.reset_edge()

    def move_right(self, amount = 40):
        for node in self.nodes:
            node.move_x(amount)
        for edge in self.edges:
            edge.reset_edge()

    def print_graph_nodes(self):
        for node in self.nodes:
            node.print_node()

    def jump(self):
        """
        function moves the coordinates of all the nodes in the graph by a random difference
        """
        x = randint(-100, 100)
        y = randint(-100, 100)
        for node in self.nodes:
            node.move_by_amount(x, y)
        for edge in self.edges:
            edge.reset_edge()

    def centralize_random_node(self):
        """
        function chooses a random node and moves it to center of screen using the function "move_node_to_center"
        """
        i = randint(0,len(self.nodes)-1)
        self.move_node_to_center(self.nodes[i])

    def move_node_to_center(self, node):
        """
        function moves the graph so that a given node's coordinates are now 'center_coor' and sets given node as 'center_node'
        :param node: a node to be moved to the center of the screen
        """
        delta_x = self.center_coor[0] - node.get_x()
        delta_y = self.center_coor[1] - node.get_y()
        for node in self.nodes:
            node.move_by_amount(delta_x,delta_y)
        for edge in self.edges:
            edge.reset_edge()
        self.center_node = node

    ### if we will need to find the closest/farthest neighbor often,
    ### we should consider adding them as KivyNode variables instead of finding them each time using the following two functions.

    def get_closest_physical_connection(self,node):
        """
        :param node: KivyNode
        :return: a KivyNode that is connected to node, and has the smallest distance from it.
        """
        min_dist = -1
        closest_node = None
        for item in node.neighbors:
            other_node = self.get_by_serial(item)
            curr_dist = node.get_distance_from_node(other_node)
            if ((curr_dist < min_dist) and (curr_dist != -1)) or (min_dist==-1):
                min_dist = curr_dist
                closest_node = other_node
        return closest_node


    def get_farthest_physical_connection(self,node):
        """
        :param node: KivyNode
        :return: a KivyNode that is connected to node, and has the largest distance from it.
        """
        max_dist = 0
        farthest_node = None
        for item in node.neighbors:
            other_node = self.get_by_serial(item)
            curr_dist = node.get_distance_from_node(other_node)
            if (curr_dist > max_dist) and (curr_dist != -1):
                max_dist = curr_dist
                farthest_node = other_node
        return farthest_node

    def resize_graph(self,new_x,new_y, keep_center = True, new_center = None):
        '''
        function sets the size of the graph to be new_x by new_y
        :param new_x: the new 'x' size of the graph
        :param new_y: the new 'y' size of the graph
        :param keep_center: if True, the graph's 'center_node' will remain the center node
        :param new_center: in the form (center_x,center_y). if given will be set as the graph's center coordinates.
        '''

        change_in_x = float(new_x)/self.real_size['max_x']
        change_in_y = float(new_y)/self.real_size['max_y']
        for node in self.nodes:
            old_size = node.node_size
            new_size = max(change_in_x,change_in_y)*old_size
            node.size = [new_size, new_size]
            node.node_size = new_size
            node.relative_move(change_in_x,change_in_y)
        for edge in self.edges:
            old_size = edge.line_width
            new_size = max(change_in_x,change_in_y)*old_size
            edge.line.width = new_size
            edge.line_width = new_size
            edge.reset_edge()

        self.real_size = {'max_x': new_x, 'max_y': new_y}

        if new_center is not None:
            self.center_coor = new_center
        if (keep_center) and (self.center_node is not None):
            self.move_node_to_center(self.center_node)
