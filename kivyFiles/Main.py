import kivy
kivy.require('1.9.1')

from kivy.core.window import Window;
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from random import randint
from NodeObject import *
from GraphObj import *
from CreateRandGraph import *
from KivyNode import *
from GraphButton import *
from KivyGraph import *
from KivyEdge import *

colors = [[1,0,0],[0,1,0],[0,0,1],[1,0,1],[1,1,0],[0,1,1]]

class GameLayout(FloatLayout):
    button_width = 100
    dim = {"min_x": button_width, "min_y": 0 ,"max_x": 800, "max_y": 600}
    original_graph = None
    kivy_graph = None

    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        kivy.core.window.Window.size = (self.dim['max_x'], self.dim['max_y'])
        self.original_graph = create_rand_graph("../config.ini")
        self.kivy_graph = KivyGraph()
        self.get_nodes()
        self.get_edges()
        self.get_buttons()
        print self.dim['min_x'],self.dim['min_y'],self.dim['max_x'],self.dim['max_y']

    def get_nodes(self):
        graph_nodes = self.original_graph.node_list
        with self.canvas:
            for node in graph_nodes:
                col = randint(0,len(colors)-1)
                Color(colors[col][0],colors[col][1],colors[col][2])
                new_node = KivyNode(node.location['x'],node.location['y'],node.serial_num)
                self.kivy_graph.add_node(new_node)

    def get_edges(self):
        edges = self.original_graph.get_connections()
        with self.canvas:
            Color(1, 1, 1)
            for edge in edges:
                node1 = self.kivy_graph.get_by_serial(edge[0])
                node2 = self.kivy_graph.get_by_serial(edge[1])
                new_edge = KivyEdge(node1,node2)
                self.kivy_graph.add_edge(new_edge)


    def get_buttons(self):
        layout = GridLayout(cols=1, col_default_width = self.button_width, col_force_default=True)
        button1 = GraphButton('button1.jpg',self.kivy_graph.move_up)
        button2 = GraphButton('button2.jpg',self.kivy_graph.move_down)
        button3 = GraphButton('button3.jpg',self.kivy_graph.move_right)
        button4 = GraphButton('button4.jpg',self.kivy_graph.move_left)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.add_widget(layout)


class GraphGameApp(App):
    def build(self):
        layout = GameLayout()
        return layout


if __name__ == "__main__":
    GraphGameApp().run()