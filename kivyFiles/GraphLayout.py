import kivy
kivy.require('1.9.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from GraphButton import MultiButton
from KivyGraph import KivyGraph
from KivyEdge import KivyEdge
from kivy.graphics import Color
from KivyNode import KivyNode
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles import Utils


class GraphLayout(FloatLayout):
    button_width = 100
    original_graph = None
    kivy_graph = None
    center_screen = (0,0)

    def __init__(self, graph, button_funcs, signal, button_lst, dim, button_width, **kwargs):

        super(GraphLayout, self).__init__(**kwargs)
        self.button_width = button_width
        self.dim = {"min_x": button_width, "min_y": 0 , "max_x": dim['max_x'], "max_y": dim['max_y']}
        self.buttons = []
        self.original_graph = graph
        self.center_screen = self.get_center_coor()
        self.kivy_graph = KivyGraph(self.center_screen,self.original_graph.size, self.dim)
        self.get_nodes()
        self.get_edges()
        self.set_button_functions(button_funcs)
        self.get_buttons(signal, button_lst)
        self.kivy_graph.centralize_random_node(False)

    def get_center_coor(self):
        """
        :return: the coordination of the center of the screen (not including the button area)
        """
        x = (self.dim['max_x'] - self.dim['min_x']) / 2 + self.button_width
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
                colour = Colours.__getattribute__(Colours,node.colour)
                Color(colour['R'],colour['G'],colour['B'])
                new_node = KivyNode(node.x, node.y, node.serial_num, colour['name'])
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

    def set_button_functions(self, buttons):
        self.button1_func = [self.kivy_graph.zoom_out, self.kivy_graph.zoom_in]
        self.button2_func = [self.kivy_graph.centralize_most_connected]
        self.button3_func = [self.kivy_graph.centralize_closest_same_color]
        self.button4_func = [self.kivy_graph.centralize_closest_neighbor_diff_color]

    def get_buttons(self, signal, button_lst):
        """
        creates a GridLayout that would hold the buttons (GraphButtons) needed for the game. each button should be
        initialized using a string representing an image to be displayed on the button and a function that will be
        responsible for the button's functionality
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        button1 = MultiButton('{}\\button1.jpg'.format(Utils.image_folder), self.button1_func, signal, button_lst, 1)
        button2 = MultiButton('{}\\button2.jpg'.format(Utils.image_folder), self.button2_func, signal, button_lst, 2)
        button3 = MultiButton('{}\\button3.jpg'.format(Utils.image_folder), self.button3_func, signal, button_lst, 3)
        button4 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button4_func, signal, button_lst, 4)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.buttons.append(button1)
        self.buttons.append(button2)
        self.buttons.append(button3)
        self.buttons.append(button4)
        self.add_widget(layout)

    def fit_graph_to_screen(self):
        self.kivy_graph.resize_graph((self.dim["max_x"]-self.dim["min_x"]),(self.dim["max_y"]-self.dim["min_y"]),20,1)
        self.kivy_graph.move_right(110)

    def set_button_status(self, status):
        for item in self.buttons:
            item.active = status

