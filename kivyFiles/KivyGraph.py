import kivy

kivy.require('1.9.1')
from kivy.uix.widget import Widget
from random import randint
from KivyNode import KivyNode


class KivyGraph(Widget):
    center_coor = (0, 0)
    nodes = None
    edges = None
    center_node = None

    def __init__(self, center, zoom_rate, screen_size, **kwargs):
        super(KivyGraph, self).__init__(**kwargs)
        self.center_coor = center
        self.zoom_rate = zoom_rate
        self.nodes = []
        self.edges = []
        self.corners = self.set_screen_corners(screen_size)

    def set_screen_corners(self, screen_size):
        """
        function calculates the corners of the visible part of the screen which are used in order to determine
        which parts of the graph are visible
        """
        min_x = screen_size["min_x"]
        min_y = screen_size["min_y"]
        max_x = int(screen_size["max_x"]*(1/self.zoom_rate))
        max_y = int(screen_size["max_y"]*(1/self.zoom_rate))

        bottom_left = KivyNode(min_x, min_y, -1, 0, 0, 'white')
        top_left = KivyNode(min_x, max_y, -1, 0, 0, 'white')
        bottom_right = KivyNode(max_x, min_y, -1, 0, 0, 'white')
        top_right = KivyNode(max_x, max_y, -1, 0, 0, 'white')

        return {"bottom_left": bottom_left, "bottom_right": bottom_right, "top_left": top_left, "top_right": top_right}

    def add_node(self, node):
        """
        function adds a given node to graph's nodes list
        """
        self.nodes.append(node)

    def add_edge(self, edge):
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

    def move_up(self, amount=5):
        self.center_node = None
        for node in self.nodes:
            node.move_y(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_y(-amount)
        self.corners["top_left"].move_y(-amount)
        self.corners["bottom_right"].move_y(-amount)
        self.corners["bottom_left"].move_y(-amount)

    def move_down(self, amount=-5):
        self.center_node = None
        for node in self.nodes:
            node.move_y(amount)
        for edge in self.edges:
            edge.reset_edge(False)
        self.corners["top_right"].move_y(-amount)
        self.corners["top_left"].move_y(-amount)
        self.corners["bottom_right"].move_y(-amount)
        self.corners["bottom_left"].move_y(-amount)

    def move_left(self, amount=-5):
        self.center_node = None
        for node in self.nodes:
            node.move_x(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_x(-amount)
        self.corners["top_left"].move_x(-amount)
        self.corners["bottom_right"].move_x(-amount)
        self.corners["bottom_left"].move_x(-amount)

    def move_right(self, amount=5):
        self.center_node = None
        for node in self.nodes:
            node.move_x(amount)
        for edge in self.edges:
            edge.reset_edge(False)

        self.corners["top_right"].move_x(-amount)
        self.corners["top_left"].move_x(-amount)
        self.corners["bottom_right"].move_x(-amount)
        self.corners["bottom_left"].move_x(-amount)

    def print_graph_nodes(self):
        for node in self.nodes:
            node.print_node()

    def jump(self, animated=True):
        """
        function moves the coordinates of all the nodes in the graph by a random difference
        """
        x = randint(-100, 100)
        y = randint(-100, 100)
        for node in self.nodes:
            node.move_by_amount(x, y, animated)
        for edge in self.edges:
            edge.reset_edge(animated)

        self.corners["top_right"].move_by_amount(-x, -y, False)
        self.corners["top_left"].move_by_amount(-x, -y, False)
        self.corners["bottom_right"].move_by_amount(-x, -y, False)
        self.corners["bottom_left"].move_by_amount(-x, -y, False)

    def move_node_to_center(self, new_center, animated=True):
        """
        moves the graph so that a given node's coordinates are now 'center_coor' and sets given node as 'center_node'
        :param new_center: a node to be moved to the center of the screen
        :param animated: if false, graph's movement will not be shown visually
        """
        delta_x = self.center_coor[0] - new_center.get_x()
        delta_y = self.center_coor[1] - new_center.get_y()

        for node in self.nodes:
            node.move_by_amount(delta_x, delta_y, animated)
        for edge in self.edges:
            edge.reset_edge(animated)
        self.center_node = new_center

        corner_x = round((1/self.zoom_rate) * -delta_x, 2)
        corner_y = round((1/self.zoom_rate) * -delta_y, 2)
        self.corners["top_right"].move_by_amount(corner_x, corner_y, False)
        self.corners["top_left"].move_by_amount(corner_x, corner_y, False)
        self.corners["bottom_right"].move_by_amount(corner_x, corner_y, False)
        self.corners["bottom_left"].move_by_amount(corner_x, corner_y, False)

    def centralize_random_node(self, animated):
        """
        function chooses a random node and moves it to center of screen using the function "move_node_to_center"
        """
        i = randint(0, len(self.nodes) - 1)
        self.move_node_to_center(self.nodes[i], animated)

    def get_most_connected(self, node_list):
        max_connections = 0
        most_connected_node = None
        for node in node_list:
            if node != self.center_node:
                curr_connections = node.get_amount_of_neighbors()
                if curr_connections > max_connections:
                    max_connections = curr_connections
                    most_connected_node = node
        return most_connected_node

    def get_closest(self, node_list, same_color):
        min_distance = -1
        closest_node = None
        color = self.center_node.get_colour()
        for node in node_list:
            if node != self.center_node:
                if (same_color == -1) or ((color == node.get_colour()) == same_color):
                    dist = self.center_node.get_distance_from_node(node)
                    if ((dist < min_distance) and (dist != -1)) or (min_distance == -1):
                        min_distance = dist
                        closest_node = node
        return closest_node

    def get_farthest(self, node_list, same_color):
        max_distance = 0
        farthest_node = None
        color = self.center_node.get_colour()
        for node in node_list:
            if node != self.center_node:
                if (same_color == -1) or ((color == node.get_colour()) == same_color):
                    dist = self.center_node.get_distance_from_node(node)
                    if dist > max_distance:
                        max_distance = dist
                        farthest_node = node
        return farthest_node

    def centralize_most_connected(self):
        node_list = self.get_onscreen_nodes(self.nodes)
        new_center = self.get_most_connected(node_list)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_most_connected_neighbor(self):
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_most_connected(node_list)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_closest_neighbor_same_color(self):
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_closest(node_list, 1)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_closest_same_color(self):
        node_list = self.get_onscreen_nodes(self.nodes)
        new_center = self.get_closest(node_list, 1)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_closest_neighbor_diff_color(self):
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_closest(node_list, 0)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def centralize_farthest_neighbor(self):
        node_list = self.get_onscreen_nodes(self.center_node.get_neighbors())
        new_center = self.get_farthest(node_list, -1)
        if new_center is not None:
            self.move_node_to_center(new_center)

    def zoom_out(self):
        self.resize_graph(self.min_size['max_x'], self.min_size['max_y'], 35, 1.4)

    def zoom_in(self):
        self.resize_graph(self.max_size['max_x'], self.max_size['max_y'], 50, 2)

    def resize_graph(self, new_x, new_y, node_size=None, edge_size=None, keep_center_node=True, new_center=None):
        """
        function sets the size of the graph to be new_x by new_y
        :param new_x: the new 'x' size of the graph
        :param new_y: the new 'y' size of the graph
        :param node_size: if set, will determine the size of the graph's nodes
        :param edge_size: if set, will determine the size of the graph's edges
        :param keep_center_node: if True, the graph's 'center_node' will remain the center node
        :param new_center: in the form (center_x,center_y). if given will be set as the graph's center coordinates.
        """

        change_in_x = float(new_x) / self.real_size['max_x']
        change_in_y = float(new_y) / self.real_size['max_y']
        for node in self.nodes:
            if node_size:
                new_size = node_size
            else:
                old_size = node.node_size
                new_size = min(change_in_x, change_in_y) * old_size
            node.size = [new_size, new_size]
            node.node_size = new_size
            node.relative_move(change_in_x, change_in_y)

        for edge in self.edges:
            if edge_size:
                new_size = edge_size
            else:
                old_size = edge.line_width
                new_size = min(change_in_x, change_in_y) * old_size
            edge.line.width = new_size
            edge.reset_edge(False)

        self.move_corners(change_in_x, change_in_y)

        if new_center:
            self.center = new_center
        if keep_center_node:
            self.move_node_to_center(self.center_node, False)

    def get_onscreen_nodes(self, node_list):
        """
        Function goes over the list of nodes in the graph and checks which ones are displayed onscreen
        :return: A list containing the nodes that are at least partially displayed onscreen.
        """
        bl = self.corners['bottom_left']
        tr = self.corners['top_right']
        displayed_nodes = []
        for node in node_list:
            node_x = node.original_location[0]
            node_y = node.original_location[1]
            node_r = node.get_radius()/2.0

            if (node_x + node_r) > bl.get_x() and (node_x - node_r) < tr.get_x() and \
                    (node_y + node_r) > bl.get_y() and (node_y - node_r) < tr.get_y():
                displayed_nodes.append(node)
        return displayed_nodes
