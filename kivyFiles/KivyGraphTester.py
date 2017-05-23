import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from GraphButton import multiButton
from KivyGraph import KivyGraph
from KivyEdge import KivyEdge
from kivy.graphics import Color
from KivyNode import KivyNode
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.NodeObject import NodeObject

Colours = [{'R':1,'G':0,'B':0,'name':"red"},{'R':0,'G':1,'B':0,'name':"green"},{'R':0,'G':0,'B':1,'name':"blue"},{'R':1,'G':0,'B':1,'name':"purple"},{'R':1,'G':1,'B':0,'name':"yellow"},{'R':0,'G':1,'B':1,'name':"light blue"}]


class GameLayout(FloatLayout):
    button_width = 100
    dim = {"min_x": button_width, "min_y": 0 ,"max_x": 400, "max_y": 200}
    original_graph = None
    kivy_graph = None
    center_screen = (0,0)


    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        kivy.core.window.Window.size = (self.dim['max_x'], self.dim['max_y'])
        self.original_graph = self.get_GraphObj()
        # self.original_graph = create_rand_graph("../config.ini")
        self.center_screen = self.get_center_coor()
        self.kivy_graph = KivyGraph(self.center_screen, self.original_graph.size, self.dim)
        self.get_nodes()
        self.get_edges()
        self.button1_func = [self.kivy_graph.zoom_out, self.kivy_graph.zoom_in]
        self.button2_func = [self.kivy_graph.centralize_most_connected_neighbor]
        self.button3_func = [self.kivy_graph.centralize_closest_neighbor_diff_color]
        self.button4_func = [self.kivy_graph.centralize_most_connected]
        self.get_buttons()
        self.kivy_graph.centralize_random_node()

    def get_center_coor(self):
        """
        :return: the coordinations of the center of the screen (not including the button area)
        """
        x = (self.dim['max_x'] - self.dim['min_x'])/2 + self.button_width
        y = (self.dim['max_y'] - self.dim['min_y']) / 2
        return (x,y)

    def get_nodes(self):
        """
        for each NodeObject from the original graph (of type GraphObj) this function creates
        an equivalent KivyNode and adds it to the kivy graph (of type KivyGraph)
        """
        graph_nodes = self.original_graph.node_list
        with self.canvas:
            for node in graph_nodes:
                colour = node.colour
                Color(colour['R'],colour['G'],colour['B'])
                new_node = KivyNode(node.x,node.y,node.serial_num,colour['name'])
                self.kivy_graph.add_node(new_node)

    def get_edges(self):
        """
        function creates a KivyEdge that represents the neighbors in the original graph (GraphObj), adds created edge to the
        kivy graph (KivyGraph), and adds the nodes (KivyNodes) connected to the edge to each other's list of neighbors
        """
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
        """
        creates a GridLayout that would hold the buttons (GraphButtons) needed for the game. each button should be
        initialized using a string representing an image to be displayed on the button and a function that will be
        responsible for the button's functionality
        """
        layout = GridLayout(cols=1, col_default_width = self.button_width, col_force_default=True)
        button1 = multiButton('button1.jpg',self.button1_func, None, [], 1)
        button2 = multiButton('button2.jpg',self.button2_func, None, [], 2)
        button3 = multiButton('button3.jpg',self.button3_func, None, [], 3)
        button4 = multiButton('button4.jpg',self.button4_func, None, [], 4)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.add_widget(layout)


    def get_GraphObj(self):
        graph = GraphObject(None,800,400,6,4,5)
        node1 = NodeObject(188, {'x': 369, 'y': 168},50,Colours[0])
        node2 = NodeObject(-55, {'x': 480, 'y': 275}, 50, Colours[1])
        node3 = NodeObject(640, {'x': 628, 'y': 169}, 50, Colours[2])
        node4 = NodeObject(206, {'x': 636, 'y': 306}, 50, Colours[3])
        node5 = NodeObject(-67, {'x': 250, 'y': 289}, 50, Colours[4])
        node6 = NodeObject(186, {'x': 184, 'y': 71}, 50, Colours[5])
        graph.node_list.append(node1)
        graph.node_list.append(node2)
        graph.node_list.append(node3)
        graph.node_list.append(node4)
        graph.node_list.append(node5)
        graph.node_list.append(node6)
        graph.connections = [(640, 188), (-55, 206), (-55, 186), (-67, 640),
                             (-67, 206), (640, 206), (-67, 186), (640, 186)]
        return graph


class GraphGameApp(App):
    def build(self):
        layout = GameLayout()
        print layout.original_graph.connections
        layout.kivy_graph.print_graph_nodes()
        return layout


