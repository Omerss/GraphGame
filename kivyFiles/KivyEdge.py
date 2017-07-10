import kivy
kivy.require('1.9.1')

from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.animation import Animation


class KivyEdge(Widget):
    node1 = None
    node2 = None
    line = None
    colour = "white"
    slope = None

    def __init__(self, node1, node2, width, **kwargs):
        super(KivyEdge, self).__init__(**kwargs)
        self.line_width = width
        if node1.get_x() < node2.get_x():
            self.node1 = node1
            self.node2 = node2
        else:
            self.node1 = node2
            self.node2 = node1

        if self.node1.x != self.node2.x:
            self.slope = abs(float(self.node2.y - self.node1.y) / (self.node2.x - self.node1.x))

        with self.canvas:
            self.line = Line(points=[self.node1.get_x(), self.node1.get_y(), self.node2.get_x(), self.node2.get_y()],
                             width=self.line_width)

    def reset_edge(self, animated):
        if animated:
            anim = Animation(points=[self.node1.get_x(), self.node1.get_y(), self.node2.get_x(), self.node2.get_y()])
            anim.start(self.line)
        else:
            self.line.points = [self.node1.get_x(), self.node1.get_y(), self.node2.get_x(), self.node2.get_y()]
