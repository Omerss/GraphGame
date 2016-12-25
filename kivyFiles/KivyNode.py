import kivy
kivy.require('1.9.1')

from kivy.graphics import Ellipse
from kivy.uix.widget import Widget
import math

class KivyNode(Widget):
    x_coor = 0
    y_coor = 0
    serial = -1
    node_size = 50
    colour = None
    neighbors = []

    def __init__(self, x_loc, y_loc, serial, colour,**kwargs):
        super(KivyNode, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        self.x_coor = x_loc
        self.y_coor = y_loc
        self.size = [self.node_size, self.node_size]
        self.pos = [self.x_coor - self.node_size / 2 ,self.y_coor - self.node_size / 2]
        self.serial = serial
        self.colour = colour
        self.neighbors = []

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)

    def get_x(self):
        return self.x_coor

    def get_y(self):
        return self.y_coor

    def add_neighbor(self,node):
        self.neighbors.append(node.serial)

    def move_up(self):
        self.y_coor += 10
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def move_down(self):
        self.y_coor -= 10
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def move_left(self):
        self.x_coor -= 10
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def move_right(self):
        self.x_coor += 10
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def move_graph(self,delta_x,delta_y):
        self.x_coor = self.x_coor + delta_x
        self.y_coor = self.y_coor + delta_y
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def move_jump(self,newX,newY):
        self.x_coor = newX
        self.y_coor = newY
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def get_neighbors(self):
        return self.neighbors

    def get_amount_of_neighbors(self):
        return len(self.neighbors)

    def get_distance_from_node(self,node):
        if node is None:
            return -1
        x = math.fabs(node.x_coor - self.x_coor)
        y = math.fabs(node.y_coor - self.y_coor)
        dist = math.sqrt(x**2 + y**2)
        return dist