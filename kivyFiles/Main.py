import kivy
kivy.require('1.9.1')

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from CreateRandGraph import create_rand_graph
from GraphButton import GraphButton
from KivyGraph import KivyGraph
from KivyEdge import KivyEdge
from random import randint
from kivy.graphics import Color
from KivyNode import KivyNode

colors = [[1,0,0],[0,1,0],[0,0,1],[1,0,1],[1,1,0],[0,1,1]]

class GameLayout(FloatLayout):
    button_width = 100
    dim = {"min_x": button_width, "min_y": 0 ,"max_x": 800, "max_y": 600}
    original_graph = None
    kivy_graph = None
    center_screen = (0,0)

    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        kivy.core.window.Window.size = (self.dim['max_x'], self.dim['max_y'])
        self.original_graph = create_rand_graph("../config.ini")
        self.center_screen = self.get_center_coor()
        self.kivy_graph = KivyGraph(self.center_screen)
        self.get_nodes()
        self.get_edges()
        self.get_buttons()
        self.kivy_graph.move_random()

    def get_center_coor(self):
        x = (self.dim['max_x'] - self.dim['min_x'])/2 + self.button_width
        y = (self.dim['max_y'] - self.dim['min_y']) / 2
        return (x,y)

    def get_nodes(self):
        graph_nodes = self.original_graph.node_list
        with self.canvas:
            for node in graph_nodes:
                colour = node.colour
                Color(colour['R'],colour['G'],colour['B'])
                new_node = KivyNode(node.location['x'],node.location['y'],node.serial_num,colour['name'])
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
                node1.add_neighbor(node2)
                node2.add_neighbor(node1)

    def get_buttons(self):
        layout = GridLayout(cols=1, col_default_width = self.button_width, col_force_default=True)
        button1 = GraphButton('button1.jpg',self.kivy_graph.move_random)
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