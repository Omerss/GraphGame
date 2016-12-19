import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
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

colors = [[1,0,0],[0,1,0],[0,0,1],[1,0,1],[1,1,0],[0,1,1]]

class GameLayout(FloatLayout):
    original_graph = None
    kivy_graph = None

    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        self.original_graph = create_rand_graph("config.ini")
        self.graph = KivyGraph()
        graph_nodes = self.original_graph.node_list
        with self.canvas:
            for node in graph_nodes:
                col = randint(0,len(colors)-1)
                Color(colors[col][0],colors[col][1],colors[col][2])
                new_node = KivyNode(node.location['x'],node.location['y'],node.serial_num)
                self.graph.add_node(new_node)

        layout = GridLayout(cols=1, col_default_width=100, col_force_default=True)
        button1 = GraphButton('button1.jpg',self.graph.move_up)
        button2 = GraphButton('button2.jpg',self.graph.move_down)
        button3 = GraphButton('button3.jpg',self.graph.move_right)
        button4 = GraphButton('button4.jpg',self.graph.move_left)
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