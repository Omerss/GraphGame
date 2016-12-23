import kivy
kivy.require('1.9.1')

from kivy.graphics import Ellipse
from kivy.uix.widget import Widget


class KivyNode(Widget):
    x_coor = 0
    y_coor = 0
    serial = -1
    node_size = 50;

    def __init__(self, x_loc, y_loc, serial,**kwargs):
        super(KivyNode, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        self.x_coor = x_loc
        self.y_coor = y_loc
        self.size = [self.node_size, self.node_size]
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]
        self.serial = serial

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)

    def get_x(self):
        return self.x_coor

    def get_y(self):
        return self.y_coor

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

    def move_graph(self,newX,newY):
        self.x_coor = self.x_coor + newX
        self.y_coor = self.y_coor + newY
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]

    def move_jump(self,newX,newY):
        self.x_coor = newX
        self.y_coor = newY
        self.pos = [self.x_coor - self.node_size / 2,self.y_coor - self.node_size / 2]
