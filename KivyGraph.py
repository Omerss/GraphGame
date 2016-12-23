import kivy
kivy.require('1.9.1')

from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from KivyNode import *
from random import randint
from KivyEdge import *


class KivyGraph(Widget):
    nodes = []
    edges = []

    def __init__(self, **kwargs):
        super(KivyGraph, self).__init__(**kwargs)


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

