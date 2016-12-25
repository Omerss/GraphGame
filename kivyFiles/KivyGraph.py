import kivy
kivy.require('1.9.1')

from kivy.uix.widget import Widget
from random import randint


class KivyGraph(Widget):
    center_coor = (0,0)
    nodes = []
    edges = []

    def __init__(self,center, **kwargs):
        super(KivyGraph, self).__init__(**kwargs)
        self.center_coor = center


    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,edge):
        self.edges.append(edge)

    def get_by_serial(self, serial):
        for node in self.nodes:
            if node.serial == serial:
                return node
        raise Exception("Node '{}' was not found in node list. Node list = {}".format(serial, self.nodes))

    def move_up(self):
        for node in self.nodes:
            node.move_up()
        for edge in self.edges:
            edge.reset_edge()


    def move_down(self):
        for node in self.nodes:
            node.move_down()
        for edge in self.edges:
            edge.reset_edge()

    def move_left(self):
        for node in self.nodes:
            node.move_left()
        for edge in self.edges:
           edge.reset_edge()

    def move_right(self):
        for node in self.nodes:
            node.move_right()
        for edge in self.edges:
            edge.reset_edge()

    def jump(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        for node in self.nodes:
            node.move_graph(x, y)
        for edge in self.edges:
            edge.reset_edge()

    def move_random(self):
        i = randint(0,len(self.nodes)-1)
        self.move_node_to_center(self.nodes[i])

    def move_node_to_center(self, node):
        delta_x = self.center_coor[0] - node.get_x()
        delta_y = self.center_coor[1] - node.get_y()
        for node in self.nodes:
            node.move_graph(delta_x,delta_y)
        for edge in self.edges:
            edge.reset_edge()


    def get_closest_physical_connection(self,node):
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
        max_dist = 0
        farthest_node = None
        for item in node.neighbors:
            other_node = self.get_by_serial(item)
            curr_dist = node.get_distance_from_node(other_node)
            if (curr_dist > max_dist) and (curr_dist != -1):
                max_dist = curr_dist
                farthest_node = other_node
        return farthest_node
