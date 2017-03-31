import kivy
kivy.require('1.9.1')

from kivy.graphics import Line
from kivy.uix.widget import Widget


class KivyEdge(Widget):
    node1 = None
    node2 = None
    line_width = 2
    line = None
    colour = "white"

    def __init__(self, node1, node2,**kwargs):
        super(KivyEdge, self).__init__(**kwargs)
        if node1.get_x() < node2.get_x():
            self.node1 = node1
            self.node2 = node2
        else:
            self.node1 = node2
            self.node2 = node1

        with self.canvas:
            self.line=Line(points=[self.node1.get_x(),self.node1.get_y(),self.node2.get_x(),self.node2.get_y()], width=self.line_width)

    def reset_edge(self):
        self.line.points = [self.node1.get_x(),self.node1.get_y(),self.node2.get_x(),self.node2.get_y()]