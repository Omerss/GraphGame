import kivy
kivy.require('1.9.1')

from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from KivyNode import *
from random import randint


class KivyGraph(Widget):
    nodes = []
    edges = []

    def __init__(self, **kwargs):
        super(KivyGraph, self).__init__(**kwargs)


    def add_node(self,node):
        self.nodes.append(node)

    def move_up(self):
        for node in self.nodes:
            node.move_up()


    def move_down(self):
        for node in self.nodes:
            node.move_down()

    def move_left(self):
        for node in self.nodes:
            node.move_left()

    def move_right(self):
        for node in self.nodes:
            node.move_right()

    def jump(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        for node in self.nodes:
            node.move_graph(x, y)
